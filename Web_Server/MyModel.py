try:
    from time import ticks_us, ticks_diff
except ImportError:
    from time import time_ns

    def ticks_us(): return int(time_ns() * 1000)
    def ticks_diff(a, b): return a - b

class RandomForestClassifier:
    """
    # RandomForestClassifier(base_estimator=deprecated, bootstrap=True, ccp_alpha=0.0, class_name=RandomForestClassifier, class_weight=None, criterion=gini, estimator=DecisionTreeClassifier(), estimator_params=('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha'), max_depth=None, max_features=sqrt, max_leaf_nodes=5, max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, n_estimators=50, n_jobs=None, num_outputs=4, oob_score=False, package_name=everywhereml.sklearn.ensemble, random_state=None, template_folder=everywhereml/sklearn/ensemble, verbose=0, warm_start=False)
    """

    def __init__(self):
        """
        Constructor
        """
        self.latency = 0
        self.predicted_value = -1

        self.votes = [0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000]

    def predict(self, x):
        """
        Predict output from input vector
        """
        self.predicted_value = -1
        started_at = ticks_us()

        self.votes = [0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000]

        idx, score = self.tree0(x)
        self.votes[idx] += score
        
        idx, score = self.tree1(x)
        self.votes[idx] += score
        
        idx, score = self.tree2(x)
        self.votes[idx] += score
        
        idx, score = self.tree3(x)
        self.votes[idx] += score
        
        idx, score = self.tree4(x)
        self.votes[idx] += score
        
        idx, score = self.tree5(x)
        self.votes[idx] += score
        
        idx, score = self.tree6(x)
        self.votes[idx] += score
        
        idx, score = self.tree7(x)
        self.votes[idx] += score
        
        idx, score = self.tree8(x)
        self.votes[idx] += score
        
        idx, score = self.tree9(x)
        self.votes[idx] += score
        
        idx, score = self.tree10(x)
        self.votes[idx] += score
        
        idx, score = self.tree11(x)
        self.votes[idx] += score
        
        idx, score = self.tree12(x)
        self.votes[idx] += score
        
        idx, score = self.tree13(x)
        self.votes[idx] += score
        
        idx, score = self.tree14(x)
        self.votes[idx] += score
        
        idx, score = self.tree15(x)
        self.votes[idx] += score
        
        idx, score = self.tree16(x)
        self.votes[idx] += score
        
        idx, score = self.tree17(x)
        self.votes[idx] += score
        
        idx, score = self.tree18(x)
        self.votes[idx] += score
        
        idx, score = self.tree19(x)
        self.votes[idx] += score
        
        idx, score = self.tree20(x)
        self.votes[idx] += score
        
        idx, score = self.tree21(x)
        self.votes[idx] += score
        
        idx, score = self.tree22(x)
        self.votes[idx] += score
        
        idx, score = self.tree23(x)
        self.votes[idx] += score
        
        idx, score = self.tree24(x)
        self.votes[idx] += score
        
        idx, score = self.tree25(x)
        self.votes[idx] += score
        
        idx, score = self.tree26(x)
        self.votes[idx] += score
        
        idx, score = self.tree27(x)
        self.votes[idx] += score
        
        idx, score = self.tree28(x)
        self.votes[idx] += score
        
        idx, score = self.tree29(x)
        self.votes[idx] += score
        
        idx, score = self.tree30(x)
        self.votes[idx] += score
        
        idx, score = self.tree31(x)
        self.votes[idx] += score
        
        idx, score = self.tree32(x)
        self.votes[idx] += score
        
        idx, score = self.tree33(x)
        self.votes[idx] += score
        
        idx, score = self.tree34(x)
        self.votes[idx] += score
        
        idx, score = self.tree35(x)
        self.votes[idx] += score
        
        idx, score = self.tree36(x)
        self.votes[idx] += score
        
        idx, score = self.tree37(x)
        self.votes[idx] += score
        
        idx, score = self.tree38(x)
        self.votes[idx] += score
        
        idx, score = self.tree39(x)
        self.votes[idx] += score
        
        idx, score = self.tree40(x)
        self.votes[idx] += score
        
        idx, score = self.tree41(x)
        self.votes[idx] += score
        
        idx, score = self.tree42(x)
        self.votes[idx] += score
        
        idx, score = self.tree43(x)
        self.votes[idx] += score
        
        idx, score = self.tree44(x)
        self.votes[idx] += score
        
        idx, score = self.tree45(x)
        self.votes[idx] += score
        
        idx, score = self.tree46(x)
        self.votes[idx] += score
        
        idx, score = self.tree47(x)
        self.votes[idx] += score
        
        idx, score = self.tree48(x)
        self.votes[idx] += score
        
        idx, score = self.tree49(x)
        self.votes[idx] += score

        # get argmax of votes
        max_vote = max(self.votes)
        self.predicted_value = next(i for i, v in enumerate(self.votes) if v == max_vote)

        self.latency = ticks_diff(ticks_us(), started_at)
        return self.predicted_value

    def latencyInMicros(self):
        """
        Get latency in micros
        """
        return self.latency

    def latencyInMillis(self):
        """
        Get latency in millis
        """
        return self.latency // 1000

    def tree0(self, x):
        """
        Random forest's tree #0
        """
        if x[1] < -0.521500002592802:
            return 1, 93.0
        else:
            if x[0] < 0.5725000128149986:
                if x[2] < 0.489499987103045:
                    return 2, 92.0
                else:
                    return 0, 74.0
            else:
                return 3, 98.0

    def tree1(self, x):
        """
        Random forest's tree #1
        """
        if x[3] < 1.1294999718666077:
            if x[0] < -0.4829999869107269:
                return 2, 96.0
            else:
                if x[0] < 0.55400001257658:
                    if x[1] < -0.5040000234730542:
                        return 1, 98.0
                    else:
                        return 0, 87.0
                else:
                    return 3, 76.0
        else:
            return 1, 98.0

    def tree2(self, x):
        """
        Random forest's tree #2
        """
        if x[4] < 1.3735000491142273:
            if x[4] < -1.7394999861717224:
                return 0, 113.0
            else:
                return 1, 93.0
        else:
            if x[0] < 0.029000000562518835:
                if x[0] < -0.49300000071525574:
                    return 2, 84.0
                else:
                    return 1, 93.0
            else:
                return 0, 113.0

    def tree3(self, x):
        """
        Random forest's tree #3
        """
        if x[1] < -0.5285000018775463:
            return 1, 92.0
        else:
            if x[2] < 0.4804999865591526:
                if x[2] < -0.007999999914318323:
                    return 2, 74.0
                else:
                    return 3, 92.0
            else:
                return 0, 99.0

    def tree4(self, x):
        """
        Random forest's tree #4
        """
        if x[1] < -0.5300000123679638:
            return 1, 95.0
        else:
            if x[2] < 0.4799999874085188:
                if x[1] < 0.024000000208616257:
                    if x[1] < 0.02049999963492155:
                        return 2, 86.0
                    else:
                        return 2, 86.0
                else:
                    return 3, 83.0
            else:
                return 0, 93.0

    def tree5(self, x):
        """
        Random forest's tree #5
        """
        if x[0] < -0.46350000600796193:
            return 2, 96.0
        else:
            if x[1] < -0.5185000021010637:
                return 1, 96.0
            else:
                if x[0] < 0.5725000128149986:
                    return 0, 84.0
                else:
                    return 3, 81.0

    def tree6(self, x):
        """
        Random forest's tree #6
        """
        if x[1] < -0.5255000125616789:
            return 1, 90.0
        else:
            if x[1] < 0.017500000074505806:
                return 2, 78.0
            else:
                if x[1] < 0.04749999940395355:
                    if x[2] < 0.5004999972879887:
                        return 3, 78.0
                    else:
                        return 0, 111.0
                else:
                    return 0, 111.0

    def tree7(self, x):
        """
        Random forest's tree #7
        """
        if x[1] < -0.521500002592802:
            return 1, 96.0
        else:
            if x[2] < 0.488500002771616:
                if x[2] < -0.006500000017695129:
                    return 2, 84.0
                else:
                    return 3, 81.0
            else:
                return 0, 96.0

    def tree8(self, x):
        """
        Random forest's tree #8
        """
        if x[2] < 0.5520000010728836:
            if x[1] < -0.521500002592802:
                return 1, 83.0
            else:
                if x[0] < 0.008000016212463379:
                    return 2, 77.0
                else:
                    return 3, 95.0
        else:
            return 0, 102.0

    def tree9(self, x):
        """
        Random forest's tree #9
        """
        if x[0] < -0.4849999868310988:
            return 2, 91.0
        else:
            if x[1] < -0.5115000028163195:
                return 1, 87.0
            else:
                if x[4] < 1.3735000491142273:
                    if x[1] < 0.04749999940395355:
                        return 3, 88.0
                    else:
                        return 0, 91.0
                else:
                    return 0, 91.0

    def tree10(self, x):
        """
        Random forest's tree #10
        """
        if x[2] < 0.5439999848604202:
            if x[5] < 1.3125:
                if x[1] < -0.5200000032782555:
                    return 1, 93.0
                else:
                    if x[0] < 0.034999996423721313:
                        return 2, 84.0
                    else:
                        return 3, 86.0
            else:
                return 2, 84.0
        else:
            return 0, 94.0

    def tree11(self, x):
        """
        Random forest's tree #11
        """
        if x[2] < 0.5529999881982803:
            if x[0] < 0.5055000027641654:
                if x[0] < -0.4630000059842132:
                    return 2, 85.0
                else:
                    return 1, 86.0
            else:
                return 3, 94.0
        else:
            return 0, 92.0

    def tree12(self, x):
        """
        Random forest's tree #12
        """
        if x[1] < -0.5270000025629997:
            return 1, 103.0
        else:
            if x[2] < 0.4804999865591526:
                if x[0] < 0.034999996423721313:
                    return 2, 66.0
                else:
                    return 3, 91.0
            else:
                return 0, 97.0

    def tree13(self, x):
        """
        Random forest's tree #13
        """
        if x[1] < -0.5200000032782555:
            return 1, 98.0
        else:
            if x[0] < 0.5725000128149986:
                if x[2] < 0.4584999866783619:
                    return 2, 76.0
                else:
                    return 0, 97.0
            else:
                return 3, 86.0

    def tree14(self, x):
        """
        Random forest's tree #14
        """
        if x[0] < 0.03249999973922968:
            return 1, 109.0
        else:
            if x[3] < -0.09150000102818012:
                if x[0] < 0.5659999847412109:
                    return 0, 84.0
                else:
                    return 3, 80.0
            else:
                if x[0] < 0.5620000138878822:
                    return 0, 84.0
                else:
                    return 3, 80.0

    def tree15(self, x):
        """
        Random forest's tree #15
        """
        if x[2] < 0.5439999848604202:
            if x[1] < -0.521500002592802:
                return 1, 100.0
            else:
                if x[2] < -0.00750000006519258:
                    return 2, 75.0
                else:
                    if x[0] < 0.034999996423721313:
                        return 2, 75.0
                    else:
                        return 3, 76.0
        else:
            return 0, 106.0

    def tree16(self, x):
        """
        Random forest's tree #16
        """
        if x[1] < -0.5305000059306622:
            return 1, 96.0
        else:
            if x[0] < -0.4380000066012144:
                return 2, 86.0
            else:
                if x[0] < 0.5725000128149986:
                    return 0, 90.0
                else:
                    return 3, 85.0

    def tree17(self, x):
        """
        Random forest's tree #17
        """
        if x[0] < 0.5710000023245811:
            if x[0] < -0.4829999869107269:
                return 2, 92.0
            else:
                if x[1] < -0.5010000024922192:
                    return 1, 76.0
                else:
                    return 0, 86.0
        else:
            return 3, 103.0

    def tree18(self, x):
        """
        Random forest's tree #18
        """
        if x[2] < 0.5439999848604202:
            if x[0] < 0.5055000027641654:
                if x[0] < -0.4834999869344756:
                    return 2, 72.0
                else:
                    return 1, 92.0
            else:
                return 3, 96.0
        else:
            return 0, 97.0

    def tree19(self, x):
        """
        Random forest's tree #19
        """
        if x[1] < -0.5285000018775463:
            return 1, 100.0
        else:
            if x[2] < 0.488500002771616:
                if x[4] < -0.8849999904632568:
                    return 2, 72.0
                else:
                    if x[2] < -0.006500000017695129:
                        return 2, 72.0
                    else:
                        return 3, 89.0
            else:
                return 0, 96.0

    def tree20(self, x):
        """
        Random forest's tree #20
        """
        if x[3] < 1.3125:
            if x[0] < -0.4834999869344756:
                return 2, 91.0
            else:
                return 3, 80.0
        else:
            if x[1] < -0.5055000027641654:
                return 1, 104.0
            else:
                if x[2] < 0.488500002771616:
                    return 3, 80.0
                else:
                    return 0, 82.0

    def tree21(self, x):
        """
        Random forest's tree #21
        """
        if x[0] < 0.03200000058859587:
            if x[3] < 1.1294999718666077:
                if x[0] < -0.48249998688697815:
                    return 2, 74.0
                else:
                    return 1, 84.0
            else:
                return 1, 84.0
        else:
            if x[3] < 1.0074999928474426:
                return 3, 87.0
            else:
                return 0, 112.0

    def tree22(self, x):
        """
        Random forest's tree #22
        """
        if x[4] < 1.5870000123977661:
            if x[0] < 0.5525000020861626:
                if x[0] < -0.4829999869107269:
                    return 2, 88.0
                else:
                    if x[0] < 0.03200000058859587:
                        return 1, 83.0
                    else:
                        return 0, 87.0
            else:
                return 3, 99.0
        else:
            return 0, 87.0

    def tree23(self, x):
        """
        Random forest's tree #23
        """
        if x[0] < 0.03249999973922968:
            if x[0] < -0.4650000059045851:
                return 2, 81.0
            else:
                return 1, 89.0
        else:
            if x[2] < 0.48800000362098217:
                return 3, 82.0
            else:
                return 0, 105.0

    def tree24(self, x):
        """
        Random forest's tree #24
        """
        if x[0] < 0.5655000060796738:
            if x[1] < -0.521500002592802:
                return 1, 97.0
            else:
                if x[2] < 0.4584999866783619:
                    return 2, 77.0
                else:
                    return 0, 91.0
        else:
            return 3, 92.0

    def tree25(self, x):
        """
        Random forest's tree #25
        """
        if x[2] < 0.5439999848604202:
            if x[5] < 0.030500000342726707:
                if x[2] < -0.005999999993946403:
                    return 2, 86.0
                else:
                    return 3, 61.0
            else:
                if x[3] < 0.762499988079071:
                    return 1, 91.0
                else:
                    return 1, 91.0
        else:
            return 0, 119.0

    def tree26(self, x):
        """
        Random forest's tree #26
        """
        if x[1] < -0.5200000032782555:
            return 1, 100.0
        else:
            if x[1] < 0.024000000208616257:
                return 2, 84.0
            else:
                if x[3] < -0.09150000102818012:
                    return 0, 83.0
                else:
                    if x[0] < 0.5470000021159649:
                        return 0, 83.0
                    else:
                        return 3, 90.0

    def tree27(self, x):
        """
        Random forest's tree #27
        """
        if x[2] < 0.5520000010728836:
            if x[2] < -0.007999999914318323:
                return 2, 90.0
            else:
                if x[1] < -0.4840000020340085:
                    return 1, 93.0
                else:
                    return 3, 77.0
        else:
            return 0, 97.0

    def tree28(self, x):
        """
        Random forest's tree #28
        """
        if x[3] < 1.3125:
            if x[2] < -0.007999999914318323:
                return 2, 94.0
            else:
                if x[2] < 0.5439999848604202:
                    if x[1] < -0.4905000068247318:
                        return 1, 86.0
                    else:
                        return 3, 88.0
                else:
                    return 0, 89.0
        else:
            return 1, 86.0

    def tree29(self, x):
        """
        Random forest's tree #29
        """
        if x[2] < 0.5520000010728836:
            if x[2] < -0.007999999914318323:
                return 2, 87.0
            else:
                if x[2] < 0.029999999329447746:
                    if x[4] < -0.45749999582767487:
                        return 3, 74.0
                    else:
                        return 3, 74.0
                else:
                    return 1, 97.0
        else:
            return 0, 99.0

    def tree30(self, x):
        """
        Random forest's tree #30
        """
        if x[4] < 0.9154999852180481:
            if x[1] < -0.5285000018775463:
                return 1, 95.0
            else:
                if x[0] < -0.43750000558793545:
                    return 2, 96.0
                else:
                    if x[0] < 0.55400001257658:
                        return 0, 85.0
                    else:
                        return 3, 81.0
        else:
            return 0, 85.0

    def tree31(self, x):
        """
        Random forest's tree #31
        """
        if x[1] < -0.521500002592802:
            return 1, 109.0
        else:
            if x[4] < 1.4345000386238098:
                if x[1] < 0.024000000208616257:
                    return 2, 66.0
                else:
                    return 3, 86.0
            else:
                if x[1] < 0.03700000047683716:
                    return 2, 66.0
                else:
                    return 0, 96.0

    def tree32(self, x):
        """
        Random forest's tree #32
        """
        if x[2] < 0.5439999848604202:
            if x[2] < -0.00750000006519258:
                return 2, 82.0
            else:
                if x[1] < -0.006000000052154064:
                    if x[3] < 4.333500027656555:
                        return 1, 77.0
                    else:
                        return 2, 82.0
                else:
                    return 3, 98.0
        else:
            return 0, 100.0

    def tree33(self, x):
        """
        Random forest's tree #33
        """
        if x[2] < 0.5439999848604202:
            if x[3] < 1.159999966621399:
                if x[0] < -0.4834999869344756:
                    return 2, 88.0
                else:
                    if x[2] < 0.027000000700354576:
                        return 3, 73.0
                    else:
                        return 1, 99.0
            else:
                return 1, 99.0
        else:
            return 0, 97.0

    def tree34(self, x):
        """
        Random forest's tree #34
        """
        if x[4] < 1.92249995470047:
            if x[0] < 0.03300000075250864:
                if x[1] < -0.5240000020712614:
                    return 1, 114.0
                else:
                    return 2, 82.0
            else:
                return 3, 74.0
        else:
            if x[0] < 0.029500000877305865:
                return 2, 82.0
            else:
                return 0, 87.0

    def tree35(self, x):
        """
        Random forest's tree #35
        """
        if x[0] < 0.03249999973922968:
            if x[2] < 0.01699999999254942:
                if x[0] < -0.4650000059045851:
                    return 2, 79.0
                else:
                    return 1, 82.0
            else:
                return 1, 82.0
        else:
            if x[0] < 0.568000003695488:
                return 0, 112.0
            else:
                return 3, 84.0

    def tree36(self, x):
        """
        Random forest's tree #36
        """
        if x[1] < -0.521500002592802:
            return 1, 96.0
        else:
            if x[3] < 1.0684999823570251:
                if x[3] < -0.09150000102818012:
                    return 2, 84.0
                else:
                    return 3, 86.0
            else:
                if x[2] < 0.48800000362098217:
                    return 3, 86.0
                else:
                    return 0, 91.0

    def tree37(self, x):
        """
        Random forest's tree #37
        """
        if x[0] < -0.4630000059842132:
            return 2, 97.0
        else:
            if x[1] < -0.5185000021010637:
                return 1, 88.0
            else:
                if x[2] < 0.4799999874085188:
                    return 3, 82.0
                else:
                    return 0, 90.0

    def tree38(self, x):
        """
        Random forest's tree #38
        """
        if x[1] < -0.5285000018775463:
            return 1, 102.0
        else:
            if x[2] < 0.4804999865591526:
                if x[0] < 0.034999996423721313:
                    return 2, 70.0
                else:
                    return 3, 95.0
            else:
                return 0, 90.0

    def tree39(self, x):
        """
        Random forest's tree #39
        """
        if x[0] < -0.4630000059842132:
            return 2, 90.0
        else:
            if x[0] < 0.03249999973922968:
                return 1, 93.0
            else:
                if x[1] < 0.045500000938773155:
                    if x[0] < 0.5710000023245811:
                        return 0, 98.0
                    else:
                        return 3, 76.0
                else:
                    return 0, 98.0

    def tree40(self, x):
        """
        Random forest's tree #40
        """
        if x[2] < -0.01899999985471368:
            return 2, 104.0
        else:
            if x[2] < 0.5439999848604202:
                if x[1] < -0.5145000061020255:
                    return 1, 86.0
                else:
                    if x[1] < -0.0044999998062849045:
                        return 2, 104.0
                    else:
                        return 3, 85.0
            else:
                return 0, 82.0

    def tree41(self, x):
        """
        Random forest's tree #41
        """
        if x[3] < -2.4105000495910645:
            return 0, 85.0
        else:
            if x[0] < 0.5700000077486038:
                if x[0] < -0.4650000059045851:
                    return 2, 83.0
                else:
                    if x[0] < 0.03249999973922968:
                        return 1, 103.0
                    else:
                        return 0, 85.0
            else:
                return 3, 86.0

    def tree42(self, x):
        """
        Random forest's tree #42
        """
        if x[2] < 0.5624999850988388:
            if x[0] < 0.5055000027641654:
                if x[2] < 0.01699999999254942:
                    if x[1] < -0.5379999801516533:
                        return 1, 85.0
                    else:
                        return 2, 84.0
                else:
                    return 1, 85.0
            else:
                return 3, 92.0
        else:
            return 0, 96.0

    def tree43(self, x):
        """
        Random forest's tree #43
        """
        if x[2] < 0.5439999848604202:
            if x[5] < 0.8849999904632568:
                if x[0] < 0.5055000027641654:
                    if x[1] < -0.5200000032782555:
                        return 1, 92.0
                    else:
                        return 2, 83.0
                else:
                    return 3, 84.0
            else:
                return 2, 83.0
        else:
            return 0, 98.0

    def tree44(self, x):
        """
        Random forest's tree #44
        """
        if x[1] < -0.5285000018775463:
            return 1, 97.0
        else:
            if x[2] < 0.4799999874085188:
                if x[2] < -0.007999999914318323:
                    return 2, 90.0
                else:
                    if x[0] < 0.036500006914138794:
                        return 2, 90.0
                    else:
                        return 3, 72.0
            else:
                return 0, 98.0

    def tree45(self, x):
        """
        Random forest's tree #45
        """
        if x[2] < -0.007999999914318323:
            return 2, 97.0
        else:
            if x[1] < -0.5115000028163195:
                return 1, 89.0
            else:
                if x[0] < 0.5710000023245811:
                    if x[1] < -0.018499999772757292:
                        return 0, 87.0
                    else:
                        return 0, 87.0
                else:
                    return 3, 84.0

    def tree46(self, x):
        """
        Random forest's tree #46
        """
        if x[3] < 1.800499975681305:
            if x[2] < 0.5439999848604202:
                if x[1] < 0.027500000782310963:
                    if x[1] < -0.5300000123679638:
                        return 1, 87.0
                    else:
                        return 2, 77.0
                else:
                    return 3, 93.0
            else:
                return 0, 100.0
        else:
            return 0, 100.0

    def tree47(self, x):
        """
        Random forest's tree #47
        """
        if x[0] < 0.03300000075250864:
            if x[2] < 0.0:
                return 2, 73.0
            else:
                return 1, 94.0
        else:
            if x[0] < 0.5710000023245811:
                return 0, 101.0
            else:
                return 3, 89.0

    def tree48(self, x):
        """
        Random forest's tree #48
        """
        if x[1] < -0.5305000059306622:
            return 1, 105.0
        else:
            if x[2] < 0.48800000362098217:
                if x[0] < 0.036500006914138794:
                    return 2, 78.0
                else:
                    return 3, 79.0
            else:
                return 0, 95.0

    def tree49(self, x):
        """
        Random forest's tree #49
        """
        if x[0] < 0.03200000058859587:
            if x[1] < -0.521500002592802:
                return 1, 105.0
            else:
                return 2, 83.0
        else:
            if x[0] < 0.5725000128149986:
                return 0, 90.0
            else:
                return 3, 79.0