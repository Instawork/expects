# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.testing import failure


with describe('be_within'):
    def it_should_pass_if_number_is_within_expected_range():
        expect(5).to(be_within(4, 7))

    def it_should_fail_if_number_is_not_within_expected_range():
        with failure(''):
            expect(1).to(be_within(4, 7))

    with context('#negated'):
        def it_should_pass_if_number_is_not_within_expected_range():
            expect(1).not_to(be_within(4, 7))

        def it_should_fail_if_number_is_within_expected_range():
            with failure(''):
                expect(5).not_to(be_within(4, 7))
