# -*- coding: utf-8 -*-

import numpy as np
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import Normalizer
from sklearn import metrics

dataset = loadtxt('/content/ia-rna/cardio.csv', delimiter=',')

X = dataset[:, 0:12]
y = dataset[:, 12]

X = Normalizer().fit(X).transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=80, shuffle=True)

model = Sequential()
model.add(Dense(100, input_dim=X.shape[1], activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(33, activation='relu'))
model.add(Dense(11, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=200, batch_size=100)

pred = (model.predict(X_test) > 0.5).astype("int32")

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

cm = confusion_matrix(y_test, pred)
print("Matriz de confusão: \n", cm)

tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()

tpr = tp / (tp + fn)
tnr = tn / (tn + fp)
acc = (tp + tn) / (tp + tn + fp + fn)

print("TPR: ", tpr)
print("TNR: ", tnr)
print("ACC: %.2f" % (acc * 100))

fpr, tpr, thresholds = metrics.roc_curve(y_test, pred, pos_label=1)
auc = metrics.auc(fpr, tpr)

plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r', label='Chance', alpha=.8)
plt.plot(fpr, tpr, color='b', label=r'ROC (AUC = %0.2f)' % (auc), lw=2, alpha=.8)
plt.suptitle('ROC Curve')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.legend(loc='lower right')
plt.show()
