from IPython.display import clear_output
from time import sleep
from keras.callbacks import ModelCheckpoint
from sklearn.metrics import log_loss # entropía cruzada
ruta = "nnet1.keras"
losses_val = []
losses_tr  = []

accs_val = []
accs_tr  = []

max_iter = 100

callbacks = [ModelCheckpoint(filepath=ruta, monitor="val_loss", verbose=1,
                             save_best_only=True)]
for epoca in range(max_iter):
    model3.fit(X_train, y_train, epochs=1, # entreno solo 1 época en training
               validation_data=(X_val, y_val), callbacks=callbacks) 
    
    loss_val, acc_val = model3.evaluate(X_val, y_val, verbose=0)
    loss_tr,  acc_tr  = model3.evaluate(X_train, y_train, verbose=0)
    losses_val.append(loss_val)
    losses_tr.append(loss_tr)
    accs_val.append(acc_val)
    accs_tr.append(acc_tr)
    
    clear_output()
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.plot(losses_tr, label="loss training")
    plt.plot(losses_val, label="loss val")
    plt.legend()
    plt.subplot(1,2,2)
    plt.plot(accs_tr, label="acc training")
    plt.plot(accs_val, label="acc val")
    plt.legend()
    
    plt.show()
    sleep(0.1)    