def migrate():
    from datetime import datetime
    
    from django.contrib.contenttypes.models import ContentType
    
    from schedule.models import Slot, Presentation, Track
    
    wed_morn_start = datetime(2011, 3, 9, 9, 0)  # 9AM Eastern
    wed_morn_end = datetime(2011, 3, 9, 12, 20)  # 12:20PM Eastern
    wed_after_start = datetime(2011, 3, 9, 14, 0)  # 2PM Eastern
    wed_after_end = datetime(2011, 3, 9, 16, 40)  # 4:40PM Eastern
    thu_morn_start = datetime(2011, 3, 10, 9, 0)  # 9AM Eastern
    thu_morn_end = datetime(2011, 3, 10, 12, 20)  # 12:20PM Eastern
    thu_after_start = datetime(2011, 3, 10, 14, 0)  # 2PM Eastern
    thu_after_end = datetime(2011, 3, 10, 16, 40)  # 4:40PM Eastern
    
    slots = [
        {
            "start": wed_morn_start,
            "end": wed_morn_end,
            "titles": [
                "Python 101",
                "Pinax Solutions",
                "web2py secrets",
                "Scientific Python Tools not only for Scientists and Engineers",
                "Distributed and Cloud computing with Python",
                "Building your own tile server using OpenStreetMap",
                "Advanced Python I"
            ]
        },
        {
            "start": wed_after_start,
            "end": wed_after_end,
            "titles": [
                "Google App Engine workshop",
                "Python For Total Beginners Using \"Learn Python The Hard Way\"",
                "Mining and Visualizing Data from the Social Web with Python",
                "Advanced Python II",
                "Packet Crafting with Python",
                "Packaging, Documenting, and Distributing your Python Codebase",
                "Geospatial Computation and Visualization Cooperative Lab",
            ]
        },
        {
            "start": thu_morn_start,
            "end": thu_morn_end,
            "titles": [
                "Hands on Beginning Python",
                "Mastering Python 3 I/O",
                "Creating GUI Applications in Python using Qt I",
                "Python/Django deployment workshop",
                "Applied machine learning in python with scikit-learn",
                "Tutorial -- Doing Data Structures in Python",
                "(Re-)Introduction to C for Pythonistas",
            ]
        },
        {
            "start": thu_after_start,
            "end": thu_after_end,
            "titles": [
                "Hands on Intermediate Python",
                "Cooking with Python 3",
                "Creating GUI Applications in Python using Qt II",
                "Faster Python Programs through Optimization",
                "Writing Python extensions in C",
                "Deploying web applications to the cloud",
                "Documenting Your Project With Sphinx",
            ]
        }
    ]
    
    for slot in slots:
        for i, title in enumerate(slot["titles"]):
            track, _ = Track.objects.get_or_create(name="Tutorial %d" % (i+1))
            s = Slot.objects.create(
                start=slot["start"],
                end=slot["end"],
                kind=ContentType.objects.get_for_model(Presentation),
                track=track,
            )
            try:
                presentation = Presentation.objects.get(title=title, presentation_type=3)
                presentation.slot = s
                presentation.save()
                print "Saved", title
            except Presentation.DoesNotExist:
                print "Missed", title
