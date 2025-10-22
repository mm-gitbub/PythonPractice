def in_autotest_we_trust(a, b):
    if a == b:
        print("Test passed")
    else:
        print("Test failed")
in_autotest_we_trust(1, True)
in_autotest_we_trust("5", "5")