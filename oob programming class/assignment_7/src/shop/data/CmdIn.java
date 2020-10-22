package shop.data;

import shop.command.UndoableCommand;

/**
 * Implementation of command to check in a video.
 * @see Data
 */
final class CmdIn implements UndoableCommand {
  private InventorySet _inventory;
  private Record _oldvalue;
  private Video _video;
  CmdIn(InventorySet inventory, Video video) {
    _inventory = inventory;
    _video = video;
    _oldvalue=_inventory.get(_video);
  }
  public boolean run() {
    // TODO 
	  try {
	      _inventory.checkIn(_video);
	      return true;
	    } 
	  catch (IllegalArgumentException e) {
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
	  _inventory.checkIn(_video);
  }
}
