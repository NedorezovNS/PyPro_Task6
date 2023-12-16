def courses_duration(courses, durations):
    courses_list = []
    ready_dict = {}
    for course, duration in zip(courses, durations):
        course_dict = {"title": course, "duration": duration}
        courses_list.append(course_dict)
    durations_dict = {}
    for ids, b in enumerate(courses_list):
        key = b['duration']
        durations_dict.setdefault(key, [])
        durations_dict[key].append(ids)
    durations_dict = dict(sorted(durations_dict.items()))
    for a, b in durations_dict.items():
        month = a
        for deep in b:
            course_id = deep
            name = courses_list[course_id]['title']
            ready_dict.setdefault(name, None)
            ready_dict[name] = month
    return ready_dict


def top_3_names(mentors):
    all_list = []
    for m in mentors:
        all_list.extend(m)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split(' ')[0]
        all_names_list.append(name)
    popular = []
    for name in all_names_list:
        popular.append((name, all_names_list.count(name)))
    popular = list(set(popular))
    popular.sort(key=lambda x: x[1], reverse=True)
    top_3 = [f"{str(x[0])}: {str(x[1])} раз(а)" for x in popular[:3]]
    result = ", ".join(top_3)
    return result


def namesake_finder(courses, mentors, durations):
    courses_list = []
    result = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    for course in courses_list:
        names_list = []
        for mentor in course["mentors"]:
            names_list.append(mentor.split(" ")[0].strip())
        unique_names = sorted(list(set(names_list)))
        same_name_list = []
        for name in unique_names:
            if names_list.count(name) > 1:
                for name_and_last in course["mentors"]:
                    if name in name_and_last:
                        same_name_list.append(name_and_last)
        if len(same_name_list) > 0:
            result.append(f'На курсе {course["title"]} есть тёзки: {", ".join(sorted(same_name_list))}')
    return '\n'.join(result)
