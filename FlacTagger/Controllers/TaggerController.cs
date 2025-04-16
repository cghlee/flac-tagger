using FlacTagger.Controllers.Interfaces;
using FlacTagger.Services.Interfaces;

namespace FlacTagger.Controllers;

internal class TaggerController : ITaggerController
{
    private ITaggerService _taggerService;
    internal TaggerController(ITaggerService taggerService)
    {
        _taggerService = taggerService;
    }
}
