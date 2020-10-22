package shop.data;

import shop.command.UndoableCommand;
import java.util.Map;

/**
 * Implementation of command to clear the inventory.
 * @see Data
 */
final class CmdClear implements UndoableCommand {
  private InventorySet _inventory;
  private Map _oldvalue;
  CmdClear(InventorySet inventory) {
    _inventory = inventory;
    //_oldvalue = _inventory.getData();  
  }
  public boolean run() {
	  try {
	      _inventory.clear();
	      return true;
	    } catch (ClassCastException e) {
	      return false;
	    }
  }
  public void undo() {
    _inventory.replaceMap(_oldvalue);
  }
  public void redo() {
    _inventory.clear();
  }
}
