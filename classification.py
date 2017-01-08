from pyAudioAnalysis import audioTrainTest as aT

aT.featureAndTrain(["./audio/metal","./audio/dance"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)