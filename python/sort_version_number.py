def version_key(version):
    """Key function for sorting versions.

    Converts version strings into a tuple of integers for comparison.

    Args:
      version: A version number string.

    Returns:
      A tuple of integers representing the version number.
    """
    return tuple(int(part) for part in version.split('.'))


assert version_key("1.0.1") == (1, 0, 1)
assert version_key("1.0") == (1, 0)
assert version_key("0.1.0") == (0, 1, 0)


def sort_version_numbers(versions):
  """Sorts a list of version numbers (strings separated by dots) in ascending order.

  Args:
    versions: A list of version numbers as strings.

  Returns:
    A sorted list of version numbers.
  """

  return sorted(versions, key=version_key)

# Example usage:
versions = ["1.0.1", "2.0", "1.10", "1.2.3", "1.1.1", "0.0.1"]
sorted_versions = sort_version_numbers(versions)
assert sorted_versions == ['0.0.1', '1.0.1', '1.1.1', '1.2.3', '1.10', '2.0']