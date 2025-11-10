import pytest
import os
import platform

from utils import (
    microk8s_disable,
    microk8s_enable,
    wait_for_pod_state,
    wait_for_installation,
)


class Testgroupeffect(object):
    @pytest.mark.skipif(
        platform.machine() == "s390x",
        reason="groupeffect tests are only relevant in x86 and arm64 architectures",
    )
    @pytest.mark.skipif(
        os.environ.get("UNDER_TIME_PRESSURE") == "True",
        reason="Skipping argocd tests as we are under time pressure",
    )
    def test_groupeffect(self):
        """
        Sets up and validates groupeffect.
        """
        print("Enabling groupeffect")
        microk8s_enable("groupeffect")
        print("Validating groupeffect")
        self.validate_groupeffect()
        print("Disabling groupeffect")
        microk8s_disable("groupeffect")

    def validate_groupeffect(self):
        """
        Validate groupeffect
        """
        wait_for_installation()
        wait_for_pod_state("", "forgejo", "running")
