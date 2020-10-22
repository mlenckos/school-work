package shop.ui;

public interface Form {
    public String getHeading();
    public String getPrompt(int i);
    public int size();
    public boolean checkInput(int i, String input);
}
