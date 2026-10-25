import pickle

for i in range(10):
    acc = pickle.load(open(f'save/cifar100/acc_task_{i}.pickle', 'rb'))
    print(f'Task {i}: {acc}')