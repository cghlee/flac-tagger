using FlacTagger.Controllers.Interfaces;
using FlacTagger.Views.Interfaces;

namespace FlacTagger.Views;

internal class TaggerView : ITaggerView
{
    private ITaggerController _taggerController;
    internal TaggerView(ITaggerController taggerController)
    {
        _taggerController = taggerController;
    }

    public void Run()
    {
        // Check for "filePaths.json" file
        // If present, import JSON for file paths
        // If not present, prompt for untagged file and output folders
        // ...
    }
}
