import argparse
import os, sys
import re
import atexit
from subprocess import Popen
from shutil import copyfile
from base64 import b64decode
from json import loads

import requests

import Utils

atexit.register(input, "Press enter to exit.")

# 1 or more digits followed by m or g, then optional b
max_heap_re = re.compile(r"^\d+[mMgG][bB]?$")


def prompt_yes_no(prompt):
    yes_inputs = {'yes', 'ye', 'y'}
    no_inputs = {'no', 'n'}
    while True:
        choice = input(prompt + " [y/n] ").lower()
        if choice in yes_inputs: 
            return True
        elif choice in no_inputs: 
            return False
        else:
            print('Please respond with "y" or "n".')


# Find Forge jar file; raise error if not found 
def find_forge_jar(forge_dir):
    for entry in os.scandir(forge_dir):
        if ".jar" in entry.name and "forge" in entry.name:
            print(f"Found forge .jar: {entry.name}")
            return entry.name
    raise FileNotFoundError(f"Could not find forge .jar in {forge_dir}.")


# Create mods folder if needed; find AP randomizer jar; return None if not found.
def find_ap_randomizer_jar(forge_dir):
    mods_dir = os.path.join(forge_dir, 'mods')
    if os.path.isdir(mods_dir):
        ap_mod_re = re.compile(r"^aprandomizer-[\d\.]+\.jar$")
        for entry in os.scandir(mods_dir):
            match = ap_mod_re.match(entry.name)
            if match:
                print(f"Found AP randomizer mod: {match.group()}")
                return match.group()
        return None
    else:
        os.mkdir(mods_dir)
        print(f"Created mods folder in {forge_dir}")
        return None


# Create APData folder if needed; clean .apmc files from APData; copy given .apmc into directory.
def replace_apmc_files(forge_dir, apmc_file):
    if apmc_file is None:
        return
    apdata_dir = os.path.join(forge_dir, 'APData')
    if not os.path.isdir(apdata_dir):
        os.mkdir(apdata_dir)
        print(f"Created APData folder in {forge_dir}")
    for entry in os.scandir(apdata_dir):
        if ".apmc" in entry.name and entry.is_file():
            os.remove(entry.path)
        print(f"Removed existing .apmc files in {apdata_dir}")
    copyfile(apmc_file, os.path.join(apdata_dir, os.path.basename(apmc_file)))
    print(f"Copied {apmc_file} to {apdata_dir}")


# Check mod version, download new mod from GitHub releases page if needed. 
def update_mod(forge_dir, ap_randomizer):
    client_releases_endpoint = "https://api.github.com/repos/KonoTyran/Minecraft_AP_Randomizer/releases"
    resp = requests.get(client_releases_endpoint)
    if resp.status_code == 200:  # OK
        latest_release = resp.json()[0]
        if ap_randomizer != latest_release['assets'][0]['name']:
            print(f"A new release of the Minecraft AP randomizer mod was found: {latest_release['assets'][0]['name']}")
            if ap_randomizer is not None:
                print(f"Your current mod is {ap_randomizer}.")
            else:
                print(f"You do not have the AP randomizer mod installed.")
            if prompt_yes_no("Would you like to update?"):
                old_ap_mod = os.path.join(forge_dir, 'mods', ap_randomizer) if ap_randomizer is not None else None
                new_ap_mod = os.path.join(forge_dir, 'mods', latest_release['assets'][0]['name'])
                print("Downloading AP randomizer mod. This may take a moment...")
                apmod_resp = requests.get(latest_release['assets'][0]['browser_download_url'])
                if apmod_resp.status_code == 200: 
                    with open(new_ap_mod, 'wb') as f:
                        f.write(apmod_resp.content)
                        print(f"Wrote new mod file to {new_ap_mod}")
                    if old_ap_mod is not None:
                        os.remove(old_ap_mod)
                        print(f"Removed old mod file from {old_ap_mod}")
                else:
                    print(f"Error retrieving the randomizer mod (status code {apmod_resp.status_code}).")
                    print(f"Please report this issue on the Archipelago Discord server.")
                    sys.exit(1)
    else:
        print(f"Error checking for randomizer mod updates (status code {resp.status_code}).")
        print(f"If this was not expected, please report this issue on the Archipelago Discord server.")
        if not prompt_yes_no("Continue anyways?"):
            sys.exit(1)


# Run the Forge server. Return process object
def run_forge_server(forge_dir, forge_server, heap_arg):
    java_exe = os.path.abspath(os.path.join('jre8', 'bin', 'java.exe'))
    if not os.path.isfile(java_exe):
        java_exe = "java"  # try to fall back on java in the PATH

    heap_arg = max_heap_re.match(max_heap).group()
    if heap_arg[-1] in ['b', 'B']:
        heap_arg = heap_arg[:-1]
    heap_arg = "-Xmx" + heap_arg

    argstring = ' '.join([java_exe, heap_arg, "-jar", forge_server, "-nogui"])
    print(f"Running Forge server: {argstring}")
    os.chdir(forge_dir)
    return Popen(argstring)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("apmc_file", default=None, help="Path to an Archipelago Minecraft data file (.apmc)")

    args = parser.parse_args()
    options = Utils.get_options()

    apmc_file = args.apmc_file
    forge_dir = options["minecraft_options"]["forge_directory"]
    max_heap = options["minecraft_options"]["max_heap_size"]

    if apmc_file is not None and not os.path.isfile(apmc_file):
        raise FileNotFoundError(f"Path {apmc_file} does not exist or could not be accessed.")
    if not os.path.isdir(forge_dir):
        raise NotADirectoryError(f"Path {forge_dir} does not exist or could not be accessed.")
    if not max_heap_re.match(max_heap):
        raise Exception(f"Max heap size {max_heap} in incorrect format. Use a number followed by M or G, e.g. 512M or 2G.")

    forge_server = find_forge_jar(forge_dir)
    ap_randomizer = find_ap_randomizer_jar(forge_dir)
    replace_apmc_files(forge_dir, apmc_file)
    update_mod(forge_dir, ap_randomizer)
    server_process = run_forge_server(forge_dir, forge_server, max_heap)
    server_process.wait()
