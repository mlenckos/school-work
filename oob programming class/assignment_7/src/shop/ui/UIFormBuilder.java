package shop.ui;

import java.util.ArrayList;
import java.util.List;

final class UIFormBuilder implements Buildform {
  private final List<Pair<String, UIFormTest>> _menu;

  public UIFormBuilder() {
    _menu = new ArrayList();
  }

  public UIForm toUIForm(String heading) {
    if (null == heading)
      throw new IllegalArgumentException();
    if (_menu.size() < 1)
      throw new IllegalStateException();

    List<Pair<String, UIFormTest>> array = new ArrayList<>();

    for (int i = 0; i < _menu.size(); i++){
      array.add(_menu.get(i));}
    return new UIForm(heading, array);
  }

  public void add(String prompt, UIFormTest test) {
    _menu.add(new Pair(prompt, test));
  }
}
