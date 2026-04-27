# jsforge.py
# Launcher for JavaScriptForge
# Created By: David Kistner (Unconditional Love) at GlyphicMind Solutions LLC.



#system imports
import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication

#folder imports
from engine.llm_engine import LLMEngine
from gui.jsforge_window import JSForgeWindow


# ---------------------------
# Main
# ---------------------------
def main():
    """
    Entry point for JavaScriptForge.
    - Loads LLM engine
    - Initializes storage directories
    - Launches JSForgeWindow
    """
    base_dir = Path(__file__).parent.resolve()

    # Paths
    manifest_path = base_dir / "models" / "manifest.yaml"
    storage_root = base_dir / "storage"

    # Ensure storage directories exist
    (storage_root / "logs").mkdir(parents=True, exist_ok=True)
    (storage_root / "pending").mkdir(parents=True, exist_ok=True)
    (storage_root / "saved").mkdir(parents=True, exist_ok=True)

    # Initialize LLM engine
    llm = LLMEngine(manifest_path)

    # Qt Application
    app = QApplication(sys.argv)

    # Launch GUI
    window = JSForgeWindow(llm, storage_root)
    window.show()

    sys.exit(app.exec_())

# --------------------------
# If name = main for window
# --------------------------
if __name__ == "__main__":
    main()

