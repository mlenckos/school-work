package shop.data;

import shop.command.UndoableCommand;

/**
 * Implementation of command to check out a video.
 * @see Data
 */
final class CmdOut implements UndoableCommand {
  private InventorySet _inventory;
  private Record _oldvalue;
  private Video _video;
  CmdOut(InventorySet inventory, Video video) {
    _inventory = inventory;
    _video = video;
    _oldvalue=_inventory.get(_video);
  }
  public boolean run() {
    // TODO
	  try {
	      _inventory.checkOut(_video);
	      return true;
	  } 
	  catch (IllegalArgumentException e) {
	      return false;
	  }
	  catch (ClassCastException e) {
	      return false;
	  } 
  }
  public void undo() {
    // TODO 
	  Record rec=_inventory.get(_video);
	  _inventory.replaceEntry(_video,_oldvalue);
	  _oldvalue=rec; 
  }
  public void redo() {
    // TODO  
	  _inventory.checkOut(_video);
  }
}
