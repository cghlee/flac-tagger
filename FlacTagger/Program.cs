using FlacTagger.Controllers;
using FlacTagger.Repositories;
using FlacTagger.Services;
using FlacTagger.Views;

namespace FlacTagger;

internal class Program
{
    internal static void Main()
    {
        TaggerRepository taggerRepository = new TaggerRepository();
        TaggerService taggerService = new TaggerService(taggerRepository);
        TaggerController taggerController = new TaggerController(taggerService);
        TaggerView taggerView = new TaggerView(taggerController);

        taggerView.Run();
    }
}
