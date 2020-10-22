package shop.ui;

public interface Buildmenu {
    public UIMenu toUIMenu(String heading);
    public void add(String prompt, UIMenuAction action);
}
