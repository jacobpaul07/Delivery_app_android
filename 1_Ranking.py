{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "colab": {
      "name": "1. Ranking.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jacobpaul07/Delivery_app_android/blob/master/1_Ranking.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WdUrxGvvDLXD",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "! git clone https://github.com/awarebayes/RecNN\n",
        "! pip install ./RecNN\n",
        "! pip install gdown\n",
        "! pip install --upgrade tqdm\n",
        "! pip install --upgrade pandas\n",
        "! pip install jupyterthemes\n",
        "\n",
        "clear_output()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bzuLRkP5DOY2",
        "colab_type": "code",
        "outputId": "5b426aa0-7ba7-4114-b36e-6e1bb7ce6b88",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 425
        }
      },
      "source": [
        "! wget http://files.grouplens.org/datasets/movielens/ml-20m.zip\n",
        "! gdown https://drive.google.com/uc?id=1EQ_zXBR3DKpmJR3jBgLvt-xoOvArGMsL\n",
        "! unzip ml-20m.zip\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "--2020-03-06 07:23:45--  http://files.grouplens.org/datasets/movielens/ml-20m.zip\n",
            "Resolving files.grouplens.org (files.grouplens.org)... 128.101.65.152\n",
            "Connecting to files.grouplens.org (files.grouplens.org)|128.101.65.152|:80... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 198702078 (189M) [application/zip]\n",
            "Saving to: ‘ml-20m.zip’\n",
            "\n",
            "ml-20m.zip          100%[===================>] 189.50M  26.2MB/s    in 7.9s    \n",
            "\n",
            "2020-03-06 07:23:54 (23.9 MB/s) - ‘ml-20m.zip’ saved [198702078/198702078]\n",
            "\n",
            "Downloading...\n",
            "From: https://drive.google.com/uc?id=1EQ_zXBR3DKpmJR3jBgLvt-xoOvArGMsL\n",
            "To: /content/ml20_pca128.pkl\n",
            "22.7MB [00:00, 227MB/s]\n",
            "Archive:  ml-20m.zip\n",
            "   creating: ml-20m/\n",
            "  inflating: ml-20m/genome-scores.csv  \n",
            "  inflating: ml-20m/genome-tags.csv  \n",
            "  inflating: ml-20m/links.csv        \n",
            "  inflating: ml-20m/movies.csv       \n",
            "  inflating: ml-20m/ratings.csv      \n",
            "  inflating: ml-20m/README.txt       \n",
            "  inflating: ml-20m/tags.csv         \n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sjvzNKRCIdt_",
        "colab_type": "code",
        "outputId": "16b68271-6307-4542-9ac7-52069db52f3f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 187
        }
      },
      "source": [
        "! git clone https://github.com/pandas-dev/pandas.git\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Cloning into 'pandas'...\n",
            "remote: Enumerating objects: 1, done.\u001b[K\n",
            "remote: Counting objects: 100% (1/1), done.\u001b[K\n",
            "remote: Total 215944 (delta 0), reused 0 (delta 0), pack-reused 215943\u001b[K\n",
            "Receiving objects: 100% (215944/215944), 177.46 MiB | 28.92 MiB/s, done.\n",
            "Resolving deltas: 100% (179620/179620), done.\n",
            "Permission denied: https://drive.google.com/uc?id=1t0LNCbqLjiLkAMFwtP8OIYU-\n",
            "Maybe you need to change permission over 'Anyone with the link'?\n",
            "tar: parsed.tar.gz: Cannot open: No such file or directory\n",
            "tar: Error is not recoverable: exiting now\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MpeVZyaj33d_",
        "colab_type": "code",
        "outputId": "b13f3477-90c6-4db4-db97-3058ac3e8b64",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        }
      },
      "source": [
        "! gdown https://drive.google.com/uc?id=1t0LNCbqLjiLkAMFwtP8OIYU-zPUCNAjK\n",
        "! tar -xvf parsed.tar.gz"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Downloading...\n",
            "From: https://drive.google.com/uc?id=1t0LNCbqLjiLkAMFwtP8OIYU-zPUCNAjK\n",
            "To: /content/parsed.tar.gz\n",
            "21.6MB [00:00, 127MB/s]\n",
            "parsed/tmdb.json\n",
            "parsed/omdb.json\n",
            "parsed/\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UB92MD0_V05O",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import torch\n",
        "from torch.utils.data import Dataset, DataLoader\n",
        "import torch.nn as nn\n",
        "import torch.nn.functional as F\n",
        "import torch.optim as optim"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BaUFQ9zwV06d",
        "colab_type": "code",
        "outputId": "29d31d1c-b19a-4ef6-d31d-02986d884d89",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 425
        }
      },
      "source": [
        "import numpy as np\n",
        "from scipy.spatial import distance\n",
        "\n",
        "from tqdm.auto import tqdm\n",
        "import pickle\n",
        "import gc\n",
        "import json\n",
        "import h5py\n",
        "import pandas as pd\n",
        "\n",
        "from IPython.display import clear_output\n",
        "import matplotlib.pyplot as plt\n",
        "%matplotlib inline\n",
        "\n",
        "# == recnn ==\n",
        "import sys\n",
        "sys.path.append(\"../../\")\n",
        "import recnn\n",
        "\n",
        "\n",
        "cuda = torch.device('cuda')\n",
        "frame_size = 10\n",
        "# https://drive.google.com/open?id=1t0LNCbqLjiLkAMFwtP8OIYU-zPUCNAjK\n",
        "meta = json.load(open('/content/parsed/omdb.json'))\n",
        "tqdm.pandas()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ImportError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tqdm/_tqdm.py\u001b[0m in \u001b[0;36mpandas\u001b[0;34m(tclass, *targs, **tkwargs)\u001b[0m\n",
            "\u001b[0;31mImportError\u001b[0m: cannot import name 'DataFrameGroupBy'",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-9-7ccdca3eb0b4>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     23\u001b[0m \u001b[0;31m# https://drive.google.com/open?id=1t0LNCbqLjiLkAMFwtP8OIYU-zPUCNAjK\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[0mmeta\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mjson\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mload\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'/content/parsed/omdb.json'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 25\u001b[0;31m \u001b[0mtqdm\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpandas\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tqdm/_tqdm.py\u001b[0m in \u001b[0;36mpandas\u001b[0;34m(tclass, *targs, **tkwargs)\u001b[0m\n",
            "\u001b[0;31mImportError\u001b[0m: cannot import name 'PanelGroupBy'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1kqzHsgvV07n",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "env = recnn.data.FrameEnv('/content/ml20_pca128.pkl',\n",
        "                         '/content/ml-20m/ratings.csv', 10, 1)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "i4VhzKwchVvR",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "e3cgDh6VV08g",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "ddpg = recnn.nn.models.Actor(1290, 128, 256).to(cuda)\n",
        "td3 = recnn.nn.models.Actor(1290, 128, 256).to(cuda)\n",
        "ddpg.load_state_dict(torch.load('/content/drive/My Drive/Colab Notebooks/ddpg_policy.pt'))\n",
        "td3.load_state_dict(torch.load('/content/drive/My Drive/Colab Notebooks/td3_policy.pt'))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0N7EciuXV09D",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "test_batch = next(iter(env.test_dataloader))\n",
        "state, action, reward, next_state, done = recnn.data.get_base_batch(test_batch)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oigOK0fBV09R",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def rank(gen_action, metric):\n",
        "    scores = []\n",
        "    for i in env.movie_embeddings_key_dict.keys():\n",
        "        if i == 0 or i == '0':\n",
        "            continue\n",
        "        scores.append([i, metric(env.movie_embeddings_key_dict[i], gen_action)])\n",
        "    scores = list(sorted(scores, key = lambda x: x[1]))\n",
        "    scores = scores[:10]\n",
        "    ids = [i[0] for i in scores]\n",
        "    for i in range(10):\n",
        "        scores[i].extend([meta[str(scores[i][0])]['omdb'][key]  for key in ['Title',\n",
        "                                'Genre', 'Language', 'Released', 'imdbRating']])\n",
        "        # scores[i][3] = ' '.join([genres_dict[i] for i in scores[i][3]])\n",
        "\n",
        "    indexes = ['id', 'score', 'Title', 'Genre', 'Language', 'Released', 'imdbRating']\n",
        "    table_dict = dict([(key,[i[idx] for i in scores]) for idx, key in enumerate(indexes)])\n",
        "    table = pd.DataFrame(table_dict)\n",
        "    return table"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": false,
        "id": "5WCmV-H-V09z",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "'0' in env.movie_embeddings_key_dict.keys()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LD8i9PapV0-D",
        "colab_type": "text"
      },
      "source": [
        "# DDPG"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "x_AeKs3xV0-J",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "ddpg_action = ddpg(state)\n",
        "# pick random action\n",
        "ddpg_action = ddpg_action[np.random.randint(0, state.size(0), 1)[0]].detach().cpu().numpy()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QSR6IwIUFMfM",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "!pip install pandas==0.23.1\n",
        "print(pd.__version__)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ROr6aR29V0-z",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from pandas.plotting import table\n",
        "import subprocess\n",
        "import matplotlib.pyplot as plt\n",
        "%matplotlib inline\n",
        "\n",
        "#from jupyterthemes import jtplot\n",
        "#jtplot.style(theme='grade3')\n",
        "\n",
        "rank(ddpg_action, distance.euclidean)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4YOnbEp9V0_D",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(ddpg_action, distance.cosine)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vQozedMeV0_j",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(ddpg_action, distance.correlation) # looks similar to cosine"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wM1qN6H8V0_9",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(ddpg_action, distance.canberra)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XJYQUTjEV1Aa",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(ddpg_action, distance.minkowski)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PLdk8AL0V1Ax",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(ddpg_action, distance.chebyshev)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tRPIStd8V1BI",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(ddpg_action, distance.braycurtis)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hNJ5PPKHV1BY",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(ddpg_action, distance.cityblock)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "p-u0ayRGV1B0",
        "colab_type": "text"
      },
      "source": [
        "# TD3"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FpTDvwnYV1B3",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "td3_action = td3(state)\n",
        "# pick random action\n",
        "td3_action = td3_action[np.random.randint(0, state.size(0), 1)[0]].detach().cpu().numpy()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Lp7P480qV1B_",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from pandas.plotting import table \n",
        "import matplotlib.pyplot as plt\n",
        "%matplotlib inline\n",
        "\n",
        "#from jupyterthemes import jtplot\n",
        "#jtplot.style(theme='grade3')\n",
        "\n",
        "rank(td3_action, distance.euclidean)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5KxqKwTcV1CW",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(td3_action, distance.cosine)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CCuhZX-6V1Co",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(td3_action, distance.correlation) # looks similar to cosine"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "W3pG-B5WV1Cy",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(td3_action, distance.canberra)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-Lx_LdbdV1C6",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(td3_action, distance.minkowski)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HqZPqZreV1DB",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(td3_action, distance.chebyshev)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3QX1Rj4JV1Dc",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(td3_action, distance.braycurtis)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GYn3lWpPV1Dm",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(td3_action, distance.cityblock)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HJNueEoGV1Dw",
        "colab_type": "text"
      },
      "source": [
        "# BCQ"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_ev7n3hXV1Dz",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "perturbator = recnn.models.bcqPerturbator(1290, 128, 256).to(cuda)\n",
        "generator = recnn.models.bcqGenerator(1290, 128, 512).to(cuda)\n",
        "\n",
        "perturbator.load_state_dict(torch.load('../../models/bcq_perturbator.pt'))\n",
        "generator.load_state_dict(torch.load('../../models/bcq_generator.pt'))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QblKv3IhV1D6",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "sampled_actions = generator.decode(state)\n",
        "perturbed_actions= perturbator(state, sampled_actions)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "328bmmKPV1D_",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "bcq_action = perturbed_actions[np.random.randint(0,\n",
        "                               sampled_actions.size(0), 1)[0]].detach().cpu().numpy()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "la0MNI74V1EW",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(bcq_action, distance.euclidean)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "u1RxhHqpV1Ep",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(bcq_action, distance.cosine)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yS_8B37eV1Ey",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(bcq_action, distance.correlation)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dezG9MC4V1E6",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(bcq_action, distance.canberra)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6P6C3225V1FN",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(bcq_action, distance.minkowski)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CPdCJKPzV1FS",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(bcq_action, distance.chebyshev)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iJ7b9ZobV1FZ",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(bcq_action, distance.braycurtis)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QQ5Vi9HAV1Fe",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rank(bcq_action, distance.cityblock)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "r1q1lqhuV1Fk",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}