from matplotlib import pyplot as plt
subjects = {
    'matan':[4, 4, 3, 5],
    'linal':[5, 4, 4, 2, 4],
    'org':[4, 4, 5],
    'istor':[5, 5, 4, 2],
}
fig, axs = plt.subplots(2,2, figsize=(10,8) )
axs =axs.ravel()     # делает одномерный массив из двумерного от сабплотов
color = ['r', 'g', 'b', 'orange']
for i, (subject, grades)  in enumerate(subjects.items()):
    axs[i].set_ylim(2,6)
    axs[i].set_yticks(range(2,6))       # если поставить область от 2 до 5 то
                            # не будет видно начало графика если первые две оценки 5
    axs[i].set_xticks(range(0,6))
    axs[i].set_ylabel('grade')
    axs[i].set_xlabel('num grade')
    axs[i].set_title(f'График оценок по предмету: {subject}')

        # print (list(range(1, 1 + len(subjects[subject])))) # выводит все итемы из словаря
    x = (list(range(1, 1 + len(subjects[subject]))))
    y = subjects[subject]
    axs[i].plot (x, y, color=color[i], label=subject)
    axs[i].legend()
plt.tight_layout()     # подправляет отступы между сабплотами

plt.show()