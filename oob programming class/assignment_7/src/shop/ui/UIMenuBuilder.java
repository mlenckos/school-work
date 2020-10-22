package shop.ui;

import java.util.ArrayList;
import java.util.List;

class UIMenuBuilder implements Buildmenu {

	  private final List<Pair<String, UIMenuAction>> _menu;

	  public UIMenuBuilder() {
	    _menu = new ArrayList();
	  }
	  public UIMenu toUIMenu(String heading) {
	    if (null == heading)
	      throw new IllegalArgumentException();
	    if (_menu.size() <= 1)
	      throw new IllegalStateException();

	    List<Pair<String, UIMenuAction>> array = new ArrayList<>();


	    for (int i = 0; i < _menu.size(); i++) {
	      array.add(_menu.get(i));
	    }
	    return new UIMenu(heading, array);
	  }
	  public void add(String prompt, UIMenuAction action) {
	    if (null == action)
	      throw new IllegalArgumentException();
	    _menu.add(new Pair<String, UIMenuAction>(prompt, action));
	  }
	}

