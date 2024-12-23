import typing
from annotated_types import MaxLen, MinLen
import pydantic


class TermBaseSchema(pydantic.BaseModel):
    """Term base schema."""

    name: typing.Annotated[
        str,
        pydantic.StringConstraints(
            strip_whitespace=True,
            min_length=1,
            max_length=255,
        ),
    ] = pydantic.Field(
        ...,
        description="The name of the term",
    )
    definition: typing.Annotated[
        str,
        MaxLen(5000),
        MinLen(1),
    ] = pydantic.Field(
        ...,
        description="The definition of the term",
    )
    topics: typing.Annotated[
        typing.Optional[
            typing.List[
                typing.Annotated[
                    str,
                    pydantic.StringConstraints(
                        to_lower=True,
                        strip_whitespace=True,
                        max_length=50,
                        min_length=1,
                    ),
                ]
            ]
        ],
        MaxLen(50),
    ] = pydantic.Field(
        default_factory=list,
        description="The topics the term belongs to",
    )
    grammatical_label: typing.Annotated[
        typing.Optional[pydantic.StrictStr],
        MaxLen(50),
        MinLen(1),
    ] = pydantic.Field(
        None,
        description="The part of speech of the term",
    )
    source_name: typing.Annotated[
        typing.Optional[str],
        MaxLen(255),
        MinLen(1),
    ] = pydantic.Field(
        None,
        description="The name of the source from which the term was obtained",
    )
    source_url: typing.Annotated[
        typing.Optional[pydantic.AnyUrl],
        pydantic.UrlConstraints(max_length=255),
    ] = pydantic.Field(
        None,
        description="The URL of the source from which the term was obtained",
    )


class TermCreateSchema(TermBaseSchema):
    """Term creation schema."""

    pass


class TermUpdateSchema(TermBaseSchema):
    """Term update schema."""

    pass


class TermSchema(TermBaseSchema):
    """Term schema. For serialization purposes only."""

    uid: pydantic.StrictStr
    verified: typing.Optional[pydantic.StrictBool] = pydantic.Field(
        False,
        description="Whether the term an its definition have been vetted and verified to be correct",
    )
    created_at: typing.Optional[pydantic.AwareDatetime] = pydantic.Field(
        description="The date and time the term was created/added"
    )
    updated_at: typing.Optional[pydantic.AwareDatetime] = pydantic.Field(
        description="The date and time the term was last updated"
    )

    class Config:
        from_attributes = True


class SearchRecordSchema(pydantic.BaseModel):
    """SearchRecord schema. For serialization purposes only."""

    uid: pydantic.StrictStr
    query: typing.Annotated[
        typing.Optional[str],
        pydantic.StringConstraints(
            strip_whitespace=True,
            max_length=255,
        ),
    ] = pydantic.Field(
        default=None,
        description="The search query made",
    )
    topics: typing.Annotated[
        typing.Optional[
            typing.List[
                typing.Annotated[
                    str,
                    pydantic.StringConstraints(
                        to_lower=True,
                        strip_whitespace=True,
                        max_length=50,
                        min_length=1,
                    ),
                ]
            ]
        ],
        MaxLen(50),
    ] = pydantic.Field(
        default=None,
        description="The topics the search was constrained to",
    )
    extradata: typing.Optional[typing.Dict[str, pydantic.JsonValue]] = pydantic.Field(
        default=None,
        description="Extra data associated with the search",
        serialization_alias="metadata",
    )
    timestamp: typing.Optional[pydantic.AwareDatetime] = pydantic.Field(
        description="The date and time the search was made"
    )

    class Config:
        from_attributes = True


class AccountSearchMetricsSchema(pydantic.BaseModel):
    """Account search metrics schema. For serialization purposes only."""

    account_id: pydantic.StrictStr
    search_count: pydantic.PositiveInt = pydantic.Field(
        default=0,
        description="The total number of searches made by the account, over a period of time",
    )
    most_searched_queries: typing.Optional[typing.Dict[pydantic.StrictStr, int]] = (
        pydantic.Field(
            default_factory=dict,
            description="Mapping of the most searched queries by the account to the number of times they were searched",
        )
    )
    most_searched_topics: typing.Optional[typing.Dict[pydantic.StrictStr, int]] = (
        pydantic.Field(
            default_factory=dict,
            description="Mapping of the most searched topics by the account to the number of account queries made on them",
        )
    )
    most_searched_words: typing.Optional[typing.Dict[pydantic.StrictStr, int]] = (
        pydantic.Field(
            default_factory=dict,
            description="Mapping of the most searched words by the account to the number of account queries made with them",
        )
    )
    period_start: typing.Optional[pydantic.AwareDatetime] = pydantic.Field(
        default=None, description="The start of the period the metrics were calculated for"
    )
    period_end: typing.Optional[pydantic.AwareDatetime] = pydantic.Field(
        default=None, description="The end of the period the metrics were calculated for"
    )



class GlobalSearchMetricsSchema(pydantic.BaseModel):
    """Global search metrics schema. For serialization purposes only."""

    search_count: pydantic.PositiveInt = pydantic.Field(
        default=0,
        description="The total number of searches made by users, over a period of time",
    )
    verified_term_count: pydantic.PositiveInt = pydantic.Field(
        default=0,
        description="The total number of verified terms in the glossary",
    )
    unverified_term_count: pydantic.PositiveInt = pydantic.Field(
        default=0,
        description="The total number of unverified terms in the glossary",
    )
    sources: typing.Optional[typing.Dict[pydantic.StrictStr, int]] = pydantic.Field(
        default_factory=dict,
        description="Mapping of the sources of terms in the glossary to the number of terms from each source",
    )
    most_searched_queries: typing.Optional[typing.Dict[pydantic.StrictStr, int]] = (
        pydantic.Field(
            default_factory=dict,
            description="Mapping of the most searched queries by users to the number of times they were searched",
        )
    )
    most_searched_topics: typing.Optional[typing.Dict[pydantic.StrictStr, int]] = (
        pydantic.Field(
            default_factory=dict,
            description="Mapping of the most searched topics by users to the number of queries made on them",
        )
    )
    most_searched_words: typing.Optional[typing.Dict[pydantic.StrictStr, int]] = (
        pydantic.Field(
            default_factory=dict,
            description="Mapping of the most searched words by users to the number of queries made with them",
        )
    )
    period_start: typing.Optional[pydantic.AwareDatetime] = pydantic.Field(
        default=None,
        description="The start of the period the metrics were calculated for",
    )
    period_end: typing.Optional[pydantic.AwareDatetime] = pydantic.Field(
        default=None,
        description="The end of the period the metrics were calculated for",
    )


__all__ = [
    "TermCreateSchema",
    "TermUpdateSchema",
    "TermSchema",
    "SearchRecordSchema",
    "AccountSearchMetricsSchema",
    "GlobalSearchMetricsSchema",
]
