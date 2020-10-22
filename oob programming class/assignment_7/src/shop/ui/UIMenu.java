package shop.ui;
import java.util.List;
/**
 * @see UIMenuBuilder
 */
final class UIMenu implements Menu {
	  private final String _heading;
	  private final List<Pair<String, UIMenuAction>> _menu;

	  UIMenu(String heading, List<Pair<String, UIMenuAction>> menu) {
	    _heading = heading;
	    _menu = menu;
	  }
	  public int size() {
	    return _menu.size();
	  }
	  public String getHeading() {
	    return _heading;
	  }
	  public String getPrompt(int i) {
	    return _menu.get(i).getPrompt();
	  }
	  public void runAction(int i) {
	    _menu.get(i).getAction().run();
	  }

}
