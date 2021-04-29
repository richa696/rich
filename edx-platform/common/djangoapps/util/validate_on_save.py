""" Utility mixin; forces models to validate *before* saving to db """


class ValidateOnSaveMixin(object):
    """
    Forces models to call their full_clean method prior to saving
    """
    def save(self, force_insert=False, force_update=False, **kwargs):
        """
        Modifies the save method to call full_clean
        """
        if not (force_insert or force_update):
            self.full_clean()
        super(ValidateOnSaveMixin, self).save(force_insert, force_update, **kwargs)  # lint-amnesty, pylint: disable=super-with-arguments
