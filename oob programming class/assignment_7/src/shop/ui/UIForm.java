package shop.ui;
import java.util.ArrayList;
import java.util.List;
import shop.ui.Pair;
// import shop.ui.UIMenu.Pair; -- cant use this fml

/**
 * @see UIFormBuilder
 * 
 * 
 */
final class UIForm implements Form{
  private final String _heading;
  private final List<Pair<String, UIFormTest>> _form;

  
  UIForm(String heading, List<Pair<String, UIFormTest>> menu) {
    _heading = heading;
    _form = menu;
  }
  public int size() {
    return _form.size();
  }
  public String getHeading() {
    return _heading;
  }
  public String getPrompt(int i) {
    return _form.get(i).getPrompt();
  }
  public boolean checkInput(int i, String input) {
  if (null == _form.get(i))
      return true;
    return _form.get(i).getTest().run(input);
  }

}
