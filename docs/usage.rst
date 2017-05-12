=====
Usage
=====

To use unach_photo_server in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'unach_photo_server.apps.UnachPhotoServerConfig',
        ...
    )

Add unach_photo_server's URL patterns:

.. code-block:: python

    from unach_photo_server import urls as unach_photo_server_urls


    urlpatterns = [
        ...
        url(r'^', include(unach_photo_server_urls)),
        ...
    ]
