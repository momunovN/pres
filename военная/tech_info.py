
from ппп.keyboards import military_ranks_info_keyboard, military_ports_info_keyboard

tech_info = {
    'tanks': {
        'name': 'Танки',
        'description': 'Основные боевые танки России',
        'characteristics': '',
        'image': '',
        'techs': [
            {
                'name': 'Т-90М',
                'description': 'Основной боевой танк России',
                'characteristics': 'Масса: 46 т, Скорость: 60 км/ч, Броня: 1000 мм',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/d/d9/T-90M.jpg'
            },
            {
                'name': 'Т-72',
                'description': 'Основной боевой танк России',
                'characteristics': 'Масса: 41 т, Скорость: 60 км/ч, Броня: 900 мм',
                'image': 'https://static.wikia.nocookie.net/warrior/images/7/72/T-72B_-_TankBiathlon14part1-01_%281%29.jpg/revision/latest?cb=20140918190511&path-prefix=ru'
            },
            {
                'name': 'Т-14 Армата',
                'description': 'Основной боевой танк России',
                'characteristics': 'Масса: 48 т, Скорость: 90 км/ч, Броня: 1200 мм',
                'image': 'https://cdn-media.tass.ru/width/1200_4ce85301/tass/m2/uploads/i/20230822/7332607.jpg'
            }
        ]

    },
    'armored_vehicles': {
        'name': 'Бронетехника',
        'description': 'Боевые машины пехоты и бронетранспортеры',
        'characteristics': '',
        'image': '',
        'techs': [
            {
                'name': 'БМП-2',
                'description': 'Боевая машина пехоты',
                'characteristics': 'Масса: 14 т, Скорость: 65 км/ч, Броня: 500 мм',
                'image': 'https://sptechnika.ru/wp-content/uploads/boevaja-mashina-pehoty-bmp-2.jpg'
            },
            {
                'name': 'БМП-3',
                'description': 'Боевая машина пехоты',
                'characteristics': 'Масса: 18 т, Скорость: 70 км/ч, Броня: 600 мм',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVfsOi4wbwenqgf4_-9M-TztCvq_BhOB5bTvx5FvhEG3pXydIrHyPvMwUwY_mcSNp4oFE&usqp=CAU'
            },
            {
                'name': 'БТР-80',
                'description': 'Бронетранспортер',
                'characteristics': 'Масса: 13 т, Скорость: 80 км/ч, Броня: 400 мм',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdv7MZ8dJQypJIK4HTSo7WMHnAbFy59_elNA&s'
            }
        ]
    },
    'artillery': {
        'name': 'Артиллерия',
        'description': 'Самоходные гаубицы и пушки',
        'characteristics': '',
        'image': '',
        'techs': [
            {
                'name': '2С19 Мста-С',
                'description': '152-мм самоходная гаубица',
                'characteristics': 'Масса: 42 т, Скорость: 60 км/ч, Дальность стрельбы: 25 км',
                'image': 'https://photo.weaponsystems.net/image/s-carousel/n-ar_sph_2s19_p04.jpg/--/img/ws/ar_sph_2s19_p04.jpg'
            },
            {
                'name': '2С35 Коалиция-СВ',
                'description': '152-мм самоходная гаубица',
                'characteristics': 'Масса: 45 т, Скорость: 60 км/ч, Дальность стрельбы: 30 км',
                'image': 'https://perevozka24.ru/img/ck_upload/5257.2S35-2021-1-1.jpg'
            }
        ]
    },
    'aviation': {
        'name': 'Авиация',
        'description': 'Многофункциональные истребители',
        'characteristics': '',
        'image': '',
        'techs': [
            {
                'name': 'Су-35С',
                'description': 'Многофункциональный истребитель',
                'characteristics': 'Масса: 19 т, Скорость: 2500 км/ч, Радиус действия: 1600 км',
                'image': 'https://topwar.ru/uploads/posts/2013-10/1381984103_wof1o.jpg'
            },
            {
                'name': 'МиГ-35',
                'description': 'Многофункциональный истребитель',
                'characteristics': 'Масса: 19 т, Скорость: 2400 км/ч, Радиус действия: 1500 км',
                'image': 'https://www.aex.ru/images/media/900/17706.jpg'
            }
        ]
    },
    'military_ports': {
        'name': 'Военные порты России',
        'description': 'Список военных портов России',
        'characteristics': 'Балтийск, Калининград, Мурманск, Новороссийск, Севастополь, Туапсе',
        'image': 'https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_65268ec1cf3464648be4b3ea_65268ec9ef7dfb61df4eaa72/scale_1200',
        'info_keyboard': military_ports_info_keyboard
    },
    'military_ranks': {
        'name': 'Военные погоны России',
        'description': 'Список военных погон России',
        'characteristics': 'Маршал, Генерал армии, \n Генерал-полковник, Генерал-лейтенант, Генерал-майор,\n Полковник, Подполковник, Майор, \n Капитан, Старший лейтенант, Лейтенант, Младший лейтенант,\n Сержант, Старшина, Старший сержант, Сержант, Младший сержант, Ефрейтор, Рядовой',
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIMd1f3xuFH-nRADrXyCo5fMz1qTeHB7qIfQ&s',
        'info_keyboard': military_ranks_info_keyboard
    }
}

