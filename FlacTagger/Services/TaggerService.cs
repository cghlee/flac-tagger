using FlacTagger.Repositories.Interfaces;
using FlacTagger.Services.Interfaces;

namespace FlacTagger.Services;

internal class TaggerService : ITaggerService
{
    private ITaggerRepository _taggerRepository;
    internal TaggerService(ITaggerRepository taggerRepository)
    {
        _taggerRepository = taggerRepository;
    }
}
