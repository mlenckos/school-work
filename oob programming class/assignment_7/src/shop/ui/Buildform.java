package shop.ui;

public interface Buildform {
    public UIForm toUIForm(String heading);
    public void add(String prompt, UIFormTest test);
}
