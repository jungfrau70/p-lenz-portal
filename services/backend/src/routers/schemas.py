from typing import List, Optional
from pydantic import BaseModel
from fastapi import Form, File, UploadFile
from datetime import date, time, datetime


class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    username: str


class TokenFullData(TokenData):
    exp: datetime


class User(BaseModel):
    id: int
    username: Optional[str] = None
    email: str
    is_active: bool


class UserInDB(User):
    hashed_password: str


class FormData(BaseModel):
    username: str
    password: str


class UserBase(BaseModel):
    email: str
    username: str = ""


class UserCreate(UserBase):
    password: str


class UserDelete(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    # icon: Optional[str] = None


# class Friend(UserBase):
#     id: int
#     is_active: bool
#     icon: str

#     class Config:
#         orm_mode = True


class User(UserBase):
    id: int
    username: str
    is_active: bool
    # icon: str
    # invite_code: Optional[str] = None
    # friends: Optional[List[Friend]] = None

    class Config:
        orm_mode = True


class Author(UserBase):
    id: int
    username: str
    is_active: bool
    # icon: str

    class Config:
        orm_mode = True


class SuccessSchema(BaseModel):
    result: bool = True


##########################

class DiscussionBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]
    discussion_topic: Optional[str]


class Discussion(DiscussionBase):
    class Config():
        orm_mode = True


class ShowDiscussion(DiscussionBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class IncidentBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    shift_start_date: Optional[date]
    shift_type: Optional[str]

    level_1_engineer1: Optional[str]
    level_1_engineer2: Optional[str]
    level_2_engineers: Optional[str]
    how_to_share: Optional[str]

    event: Optional[str]
    action: Optional[str]
    status: Optional[str]
    ticket_no: Optional[str]
    escalated_to_l3: Optional[str]
    comment: Optional[str]

    occurred_at: Optional[datetime]
    acknowledged_at: Optional[datetime]
    propogated_at: Optional[datetime]
    resolved_at: Optional[datetime]


class Incident(IncidentBase):
    class Config():
        orm_mode = True


class ShowIncident(IncidentBase):
    id: int
    reviewer: Optional[str]
    creator: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class IssueBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    title: Optional[str]
    description: Optional[str]
    action: Optional[str]

    occurred_at: Optional[datetime]
    resolved_at: Optional[datetime]


class Issue(IssueBase):
    class Config():
        orm_mode = True


class ShowIssue(IssueBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class ProblemBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]
    impact: Optional[str]

    title: Optional[str]
    description: Optional[str]
    action: Optional[str]
    person_in_charge: Optional[str]
    ticket_no: Optional[str]

    rca_desc: Optional[str]
    review_desc: Optional[str]

    occurred_at: Optional[datetime]
    reviewed_at: Optional[datetime]


class Problem(ProblemBase):
    class Config():
        orm_mode = True


class ShowProblem(ProblemBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class ChangeBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    ticket_no: Optional[str]
    title: Optional[str]
    description: Optional[str]


class Change(ChangeBase):
    class Config():
        orm_mode = True


class ShowChange(ChangeBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class RequestBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    ticket_no: Optional[str]
    title: Optional[str]
    description: Optional[str]
    work_type: Optional[str]


class Request(RequestBase):
    class Config():
        orm_mode = True


class ShowRequest(RequestBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class CapacityBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    category: Optional[str]
    ticket_no: Optional[str]
    title: Optional[str]
    description: Optional[str]


class Capacity(CapacityBase):
    class Config():
        orm_mode = True


class ShowCapacity(CapacityBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class BackupBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    db_type: Optional[str]
    instance_name: Optional[str]
    instance_ip: Optional[str]
    freq_full_archive: Optional[str]
    comment: Optional[str]


class Backup(BackupBase):
    class Config():
        orm_mode = True


class ShowBackup(BackupBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class InstanceBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    status: Optional[str]
    count: Optional[int]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class Instance(InstanceBase):
    class Config():
        orm_mode = True


class ShowInstance(InstanceBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class KubernetesBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    status: Optional[str]
    cluster_name: Optional[str]
    node_type: Optional[str]
    node_name: Optional[str]
    node_ips: Optional[str]
    api_vip: Optional[str]
    flavor: Optional[str]
    network_zone: Optional[str]
    contacts: Optional[str]
    k8s_version: Optional[str]
    monitoring_agent: Optional[str]

    api_cert_expired_date: Optional[datetime]
    ca_cert_expired_date: Optional[datetime]
    etcd_cert_expired_date: Optional[datetime]


class Kubernetes(KubernetesBase):
    class Config():
        orm_mode = True


class ShowKubernetes(KubernetesBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class DatabaseBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    db_type: Optional[str]
    count: Optional[int]
    status: Optional[str]


class Database(DatabaseBase):
    class Config():
        orm_mode = True


class ShowDatabase(DatabaseBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class LicenseBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    vendor: Optional[str]
    license_type: Optional[str]
    status: Optional[str]
    instance_name: Optional[str]
    comment: Optional[str]
    installed_at: Optional[str]

    occurred_at: Optional[datetime]
    resolved_at: Optional[datetime]


class License(LicenseBase):
    class Config():
        orm_mode = True


class ShowLicense(LicenseBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class VulnerabilityBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    ticket_no: Optional[str]
    title: Optional[str]
    task_type: Optional[str]


class Vulnerability(VulnerabilityBase):
    class Config():
        orm_mode = True


class ShowVulnerability(VulnerabilityBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class PreventiveBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    freq: Optional[str]
    vendor: Optional[str]
    title: Optional[str]
    description: Optional[str]


class Preventive(PreventiveBase):
    class Config():
        orm_mode = True


class ShowPreventive(PreventiveBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True


class ReportBase(BaseModel):
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    vendor: Optional[str]
    report_name: Optional[str]
    comment: Optional[str]


class Report(ReportBase):
    class Config():
        orm_mode = True


class ShowReport(ReportBase):
    id: int
    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True
