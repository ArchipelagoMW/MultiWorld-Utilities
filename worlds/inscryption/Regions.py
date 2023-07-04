from typing import Dict, Set, List

inscryption_regions: Dict[str, Set[str]] = {
    "Menu": {"Act 1", "Act 2", "Act 3"},
    "Act 1": {"Menu"},
    "Act 2": {"Menu", "Act 3"},
    "Act 3": {"Menu", "Epilogue"},
    "Epilogue": {"Menu"}
}
