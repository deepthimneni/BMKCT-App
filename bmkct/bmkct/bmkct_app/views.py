from django.shortcuts import render

# Create your views here.
def index(request):
    groups = ["Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2", "Some-Text-1", "Some-Text-2"]
    return render(request, 'index.html', {'groups': groups})

def group_list(request, group):
    group_list = [{
        'group_name': 'Some-Text-1',
        'box_name': 'Box-1',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec semper, leo sit amet varius ullamcorper, odio felis finibus sapien, et molestie elit purus vitae est. Aenean diam erat, interdum et suscipit et, hendrerit et arcu. Nulla gravida, metus et auctor feugiat, magna magna efficitur tellus, sit amet blandit libero urna ut lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse magna odio, mollis at sem in, scelerisque convallis est. Vestibulum vitae purus lacinia, auctor ex et, aliquet nisl. Nam quam quam, imperdiet quis urna eu, rhoncus congue augue.'
    },
    {
        'group_name': 'Some-Text-1',
        'box_name': 'Box-1',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec semper, leo sit amet varius ullamcorper, odio felis finibus sapien, et molestie elit purus vitae est. Aenean diam erat, interdum et suscipit et, hendrerit et arcu. Nulla gravida, metus et auctor feugiat, magna magna efficitur tellus, sit amet blandit libero urna ut lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse magna odio, mollis at sem in, scelerisque convallis est. Vestibulum vitae purus lacinia, auctor ex et, aliquet nisl. Nam quam quam, imperdiet quis urna eu, rhoncus congue augue.'
    },
    {
        'group_name': 'Some-Text-1',
        'box_name': 'Box-1',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec semper, leo sit amet varius ullamcorper, odio felis finibus sapien, et molestie elit purus vitae est. Aenean diam erat, interdum et suscipit et, hendrerit et arcu. Nulla gravida, metus et auctor feugiat, magna magna efficitur tellus, sit amet blandit libero urna ut lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse magna odio, mollis at sem in, scelerisque convallis est. Vestibulum vitae purus lacinia, auctor ex et, aliquet nisl. Nam quam quam, imperdiet quis urna eu, rhoncus congue augue.'
    },
    {
        'group_name': 'Some-Text-1',
        'box_name': 'Box-1',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec semper, leo sit amet varius ullamcorper, odio felis finibus sapien, et molestie elit purus vitae est. Aenean diam erat, interdum et suscipit et, hendrerit et arcu. Nulla gravida, metus et auctor feugiat, magna magna efficitur tellus, sit amet blandit libero urna ut lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse magna odio, mollis at sem in, scelerisque convallis est. Vestibulum vitae purus lacinia, auctor ex et, aliquet nisl. Nam quam quam, imperdiet quis urna eu, rhoncus congue augue.'
    },
    {
        'group_name': 'Some-Text-1',
        'box_name': 'Box-1',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec semper, leo sit amet varius ullamcorper, odio felis finibus sapien, et molestie elit purus vitae est. Aenean diam erat, interdum et suscipit et, hendrerit et arcu. Nulla gravida, metus et auctor feugiat, magna magna efficitur tellus, sit amet blandit libero urna ut lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse magna odio, mollis at sem in, scelerisque convallis est. Vestibulum vitae purus lacinia, auctor ex et, aliquet nisl. Nam quam quam, imperdiet quis urna eu, rhoncus congue augue.'
    }]
    return render(request, 'list.html', {'group_list': group_list})