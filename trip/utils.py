from slugify import slugify


def generate_unique_slug(klass, field):
    main_slug = slugify(field)
    unique_slug = main_slug
    counter = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{main_slug}-{counter}'
        counter += 1
    return unique_slug
