from ._utils import *


settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'armstrong.core.arm_content',
        'armstrong.core.arm_content.tests.arm_content_support',
        'armstrong.apps.embedded_video',
    ),
    'AUTH_PROFILE_MODULE': 'arm_content_support.SimpleProfile',
    'ROOT_URLCONF': '',
    'ARMSTRONG_EXTERNAL_VIDEO_BACKEND': 'armstrong.core.arm_content.video.backends.YouTubeBackend'
}


@task
def clean():
    local('find . -name "*.py[co]" -exec rm {} \;')


@task
def pep8():
    local('find ./armstrong -name "*.py" | xargs pep8', capture=False)


@task
def test():
    with html_coverage_report():
        try:
            run_tests(settings, 'arm_content_support', 'arm_content', 'embedded_video')
        except Exception, e:
            import ipdb;ipdb.set_trace()


@task
def runserver():
    from d51.django.virtualenv.base import VirtualEnvironment
    runner = VirtualEnvironment()
    runner.run(settings)
    runner.call_command("syncdb")
    runner.call_command("runserver")
