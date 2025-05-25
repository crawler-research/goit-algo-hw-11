class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    # Копіюємо множину предметів для роботи
    remaining_subjects = subjects.copy()
    selected_teachers = []
    
    while remaining_subjects:
        best_teacher = None
        max_coverage = 0
        
        # Знаходимо викладача, який покриває найбільше предметів
        for teacher in teachers:
            # Кількість предметів, які цей викладач може покрити з тих, що залишились
            coverage = len(teacher.can_teach_subjects & remaining_subjects)
            
            if coverage > max_coverage:
                max_coverage = coverage
                best_teacher = teacher
            elif coverage == max_coverage and best_teacher is not None:
                # Якщо покриття однакове, обираємо наймолодшого
                if teacher.age < best_teacher.age:
                    best_teacher = teacher
        
        # Якщо не знайшли викладача, який може покрити хоча б один предмет
        if best_teacher is None or max_coverage == 0:
            return None
        
        # Призначаємо предмети викладачу
        subjects_to_assign = best_teacher.can_teach_subjects & remaining_subjects
        best_teacher.assigned_subjects = subjects_to_assign
        
        # Додаємо викладача до розкладу
        selected_teachers.append(best_teacher)
        
        # Видаляємо покриті предмети
        remaining_subjects -= subjects_to_assign
        
        # Видаляємо викладача зі списку доступних
        teachers.remove(best_teacher)
    
    return selected_teachers

if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    
    # Створення списку викладачів
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", 
                {'Математика', 'Фізика'}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", 
                {'Хімія'}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", 
                {'Інформатика', 'Математика'}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", 
                {'Біологія', 'Хімія'}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", 
                {'Фізика', 'Інформатика'}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", 
                {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
        
        # Перевірка покриття всіх предметів
        covered_subjects = set()
        for teacher in schedule:
            covered_subjects.update(teacher.assigned_subjects)
        
        print(f"Всього викладачів у розкладі: {len(schedule)}")
        print(f"Покриті предмети: {covered_subjects}")
        print(f"Усі предмети покриті: {'Так' if covered_subjects == subjects else 'Ні'}")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")