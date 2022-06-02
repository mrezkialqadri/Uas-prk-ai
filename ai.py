import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class fuzzyNilai:
     
    def __init__(self):
     
        self.forum = ctrl.Antecedent(np.arange(0, 11, 1), 'forum')
        self.disiplin = ctrl.Antecedent(np.arange(0, 11, 1), 'disiplin')
        self.NilaiQuizUjian = ctrl.Antecedent(np.arange(0, 11, 1), 'nilai')
        self.NilaiAkhir = ctrl.Consequent(np.arange(0, 101, 1), 'nilaiakhir')
         
    def membership(self):
        self.forum.automf(3)
        self.disiplin.automf(3)
        self.NilaiQuizUjian.automf(3)
         
    def customMembership(self):
        self.membership()
        self.NilaiAkhir['kecil'] = fuzz.trimf(self.NilaiAkhir.universe,[0,0,80])
        self.NilaiAkhir['sedang'] = fuzz.trimf(self.NilaiAkhir.universe,[60,80,100])
        self.NilaiAkhir['tinggi'] = fuzz.trimf(self.NilaiAkhir.universe,[80,100,100])
         
    def rule(self):
        self.membership()
        self.customMembership()
        self.rule1 = ctrl.Rule(self.forum['poor'] | self.disiplin['poor'] | self.NilaiQuizUjian['poor'], self.NilaiAkhir['kecil'])
         
        self.rule2 = ctrl.Rule(self.forum['good'] | self.NilaiQuizUjian['good'], self.NilaiAkhir['tinggi'])
         
        self.rule3 = ctrl.Rule(self.forum['average'] | self.disiplin['average'], self.NilaiAkhir['sedang'])
         
        self.rule4 = ctrl.Rule(self.disiplin['good'], self.NilaiAkhir['tinggi'])
         
         
         
    def controlSystem(self):
        self.rule()
        nilai_ctrl = ctrl.ControlSystem([self.rule1, self.rule2, self.rule3, self.rule4])
        self.scoring = ctrl.ControlSystemSimulation(nilai_ctrl)
         
        self.scoring.input['forum'] = 4
        self.scoring.input['disiplin'] = 4
        self.scoring.input['nilai'] = 1
         
        self.scoring.compute()
         
    def result(self):
        self.controlSystem()
        print(self.scoring.output['nilaiakhir'])
        self.NilaiAkhir.view(sim=self.scoring)