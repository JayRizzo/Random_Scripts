"""UUID Example.

Answer for: https://stackoverflow.com/q/52290160/1896134
Python string formatting and UUID.
"""
import pandas as pd
import uuid

df = pd.read_csv('media.csv', sep=',')


def convert_row(row):
    """Convert Row Example."""
    u = str(uuid.uuid4())
    return """<video>
    <videoType fileUID={} name=\"\">
        <locationType></locationType>
        <type>{}</type>
        <format>{}</format>
        <year>{}</year>
    </videoType>
</video>""".format(u, row[0], row[1], row[2], row[3])

print("\n".join(df.apply(convert_row, axis=1)))
