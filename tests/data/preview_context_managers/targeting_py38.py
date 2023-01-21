with \
     make_context_manager1() as cm1, \
     make_context_manager2() as cm2, \
     make_context_manager3() as cm3, \
     make_context_manager4() as cm4 \
:
    pass


with \
     make_context_manager1() as cm1, \
     make_context_manager2(), \
     make_context_manager3() as cm3, \
     make_context_manager4() \
:
    pass


with \
     new_new_new1() as cm1, \
     new_new_new2() \
:
    pass


# output


with make_context_manager1() as cm1, make_context_manager2() as cm2, make_context_manager3() as cm3, make_context_manager4() as cm4:
    pass


with make_context_manager1() as cm1, make_context_manager2(), make_context_manager3() as cm3, make_context_manager4():
    pass


with new_new_new1() as cm1, new_new_new2():
    pass
