using System.Threading.Tasks;
using Windows.UI.Xaml.Controls;

namespace AverageCalculator
{
    internal class InputDialog
    {
    }
    public static async Task<string> Show(string message, string title = "Input")
    {
        TextBox inputBox = new TextBox();
        ContentDialog dialog = new ContentDialog
        {
            Title = title,
            Content = inputBox,
            PrimaryButtonText = "OK",
            CloseButtonText = "Annulla"
        };

        ContentDialogResult result = await dialog.ShowAsync();
        if (result == ContentDialogResult.Primary)
        {
            return inputBox.Text;
        }

        return null;
    }
}