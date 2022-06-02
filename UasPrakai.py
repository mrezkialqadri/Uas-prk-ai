      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import skfuzzy as fuzz\n",
        "from skfuzzy import control as ctrl\n",
        "\n",
        "class fuzzyNilai:\n",
        "     \n",
        "    def __init__(self):\n",
        "     \n",
        "        self.forum = ctrl.Antecedent(np.arange(0, 11, 1), 'forum')\n",
        "        self.disiplin = ctrl.Antecedent(np.arange(0, 11, 1), 'disiplin')\n",
        "        self.NilaiQuizUjian = ctrl.Antecedent(np.arange(0, 11, 1), 'nilai')\n",
        "        self.NilaiAkhir = ctrl.Consequent(np.arange(0, 101, 1), 'nilaiakhir')\n",
        "         \n",
        "    def membership(self):\n",
        "        self.forum.automf(3)\n",
        "        self.disiplin.automf(3)\n",
        "        self.NilaiQuizUjian.automf(3)\n",
        "         \n",
        "    def customMembership(self):\n",
        "        self.membership()\n",
        "        self.NilaiAkhir['kecil'] = fuzz.trimf(self.NilaiAkhir.universe,[0,0,80])\n",
        "        self.NilaiAkhir['sedang'] = fuzz.trimf(self.NilaiAkhir.universe,[60,80,100])\n",
        "        self.NilaiAkhir['tinggi'] = fuzz.trimf(self.NilaiAkhir.universe,[80,100,100])\n",
        "         \n",
        "    def rule(self):\n",
        "        self.membership()\n",
        "        self.customMembership()\n",
        "        self.rule1 = ctrl.Rule(self.forum['poor'] | self.disiplin['poor'] | self.NilaiQuizUjian['poor'], self.NilaiAkhir['kecil'])\n",
        "         \n",
        "        self.rule2 = ctrl.Rule(self.forum['good'] | self.NilaiQuizUjian['good'], self.NilaiAkhir['tinggi'])\n",
        "         \n",
        "        self.rule3 = ctrl.Rule(self.forum['average'] | self.disiplin['average'], self.NilaiAkhir['sedang'])\n",
        "         \n",
        "        self.rule4 = ctrl.Rule(self.disiplin['good'], self.NilaiAkhir['tinggi'])\n",
        "         \n",
        "         \n",
        "         \n",
        "    def controlSystem(self):\n",
        "        self.rule()\n",
        "        nilai_ctrl = ctrl.ControlSystem([self.rule1, self.rule2, self.rule3, self.rule4])\n",
        "        self.scoring = ctrl.ControlSystemSimulation(nilai_ctrl)\n",
        "         \n",
        "        self.scoring.input['forum'] = 4\n",
        "        self.scoring.input['disiplin'] = 4\n",
        "        self.scoring.input['nilai'] = 1\n",
        "         \n",
        "        self.scoring.compute()\n",
        "         \n",
        "    def result(self):\n",
        "        self.controlSystem()\n",
        "        print(self.scoring.output['nilaiakhir'])\n",
        "        self.NilaiAkhir.view(sim=self.scoring)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 133
        },
        "id": "paE_Sh2phxEu",
        "outputId": "2810a29b-cfe5-43f0-891e-eed409813418"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-14-985c58b52285>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    public class FuzzyTsukamoto {\u001b[0m\n\u001b[0m               ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    }
  ]
}
