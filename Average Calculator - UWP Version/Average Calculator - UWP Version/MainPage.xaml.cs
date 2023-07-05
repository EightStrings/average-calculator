using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;

namespace AverageCalculator
{
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();
        }

        private async void CalculateButton_Click(object sender, RoutedEventArgs e)
        {
            // Mostra una finestra di dialogo per selezionare le materie
            string selectedSubjects = await InputDialog.ShowSubjects("Seleziona le materie:");

            // Mostra una finestra di dialogo per inserire il numero di voti
            string inputCount = await InputDialog.ShowCount("Inserisci il numero di voti:");

            // Esegui le operazioni necessarie con i dati ottenuti
            if (!string.IsNullOrEmpty(selectedSubjects) && !string.IsNullOrEmpty(inputCount))
            {
                // Esempio: Calcola la media dei voti
                int count = int.Parse(inputCount);
                double total = 0;

                for (int i = 0; i < count; i++)
                {
                    // Mostra una finestra di dialogo per inserire il voto
                    string inputGrade = await InputDialog.ShowGrade($"Inserisci il voto #{i + 1} per {selectedSubjects}:");

                    if (double.TryParse(inputGrade, out double grade))
                    {
                        total += grade;
                    }
                    else
                    {
                        // Il voto non è un numero valido
                        ResultTextBlock.Text = "Voto non valido!";
                        return;
                    }
                }

                double average = total / count;

                // Aggiorna l'interfaccia utente con il risultato
                ResultTextBlock.Text = $"Media per {selectedSubjects}: {average}";
            }
            else
            {
                // L'utente ha annullato una delle finestre di dialogo o non ha inserito i dati necessari
                ResultTextBlock.Text = "Operazione annullata o dati mancanti!";
            }
        }
    }
}
