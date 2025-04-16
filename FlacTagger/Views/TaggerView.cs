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
}
