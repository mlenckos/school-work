package shop.ui;

public class UIFactory {
  private UIFactory() {}
  static private UI _UI = new PopupUI();
  //static private UI _UI = new TextUI();
  static public UI ui () {
    return _UI;
  }
  // make some generic stuff legooooooo

  static public UIMenu newUIMenu (UIMenuBuilder a, String b) {
    return a.toUIMenu(b);
  }

  static public UIForm newUIForm (Buildform a, String b) {
    return a.toUIForm(b);
  }
  static public Buildmenu newUIMenuBuilder () {
	return new UIMenuBuilder();
  }
  static public Buildform newUIFormBuilder () {
	return new UIFormBuilder();
  }
}
