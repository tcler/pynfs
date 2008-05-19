# Generated by rpcgen.py from gss.x on Thu Feb 22 16:04:32 2007
RPCSEC_GSS_DATA = 0
RPCSEC_GSS_INIT = 1
RPCSEC_GSS_CONTINUE_INIT = 2
RPCSEC_GSS_DESTROY = 3
rpc_gss_proc_t = {
    0 : 'RPCSEC_GSS_DATA',
    1 : 'RPCSEC_GSS_INIT',
    2 : 'RPCSEC_GSS_CONTINUE_INIT',
    3 : 'RPCSEC_GSS_DESTROY',
}
rpc_gss_svc_none = 1
rpc_gss_svc_integrity = 2
rpc_gss_svc_privacy = 3
rpc_gss_service_t = {
    1 : 'rpc_gss_svc_none',
    2 : 'rpc_gss_svc_integrity',
    3 : 'rpc_gss_svc_privacy',
}
RPCSEC_GSS_VERS_1 = 1
MAXSEQ = 0x80000000L
GSS_S_COMPLETE = 0x00000000L
GSS_S_CONTINUE_NEEDED = 0x00000001L
GSS_S_DUPLICATE_TOKEN = 0x00000002L
GSS_S_OLD_TOKEN = 0x00000004L
GSS_S_UNSEQ_TOKEN = 0x00000008L
GSS_S_GAP_TOKEN = 0x00000010L
GSS_S_BAD_MECH = 0x00010000L
GSS_S_BAD_NAME = 0x00020000L
GSS_S_BAD_NAMETYPE = 0x00030000L
GSS_S_BAD_BINDINGS = 0x00040000L
GSS_S_BAD_STATUS = 0x00050000L
GSS_S_BAD_MIC = 0x00060000L
GSS_S_BAD_SIG = 0x00060000L
GSS_S_NO_CRED = 0x00070000L
GSS_S_NO_CONTEXT = 0x00080000L
GSS_S_DEFECTIVE_TOKEN = 0x00090000L
GSS_S_DEFECTIVE_CREDENTIAL = 0x000a0000L
GSS_S_CREDENTIALS_EXPIRED = 0x000b0000L
GSS_S_CONTEXT_EXPIRED = 0x000c0000L
GSS_S_FAILURE = 0x000d0000L
GSS_S_BAD_QOP = 0x000e0000L
GSS_S_UNAUTHORIZED = 0x000f0000L
GSS_S_UNAVAILABLE = 0x00100000L
GSS_S_DUPLICATE_ELEMENT = 0x00110000L
GSS_S_NAME_NOT_MN = 0x00120000L
GSS_S_CALL_INACCESSIBLE_READ = 0x01000000L
GSS_S_CALL_INACCESSIBLE_WRITE = 0x02000000L
GSS_S_CALL_BAD_STRUCTURE = 0x03000000L
gss_major_codes = {
    0x00000000L : 'GSS_S_COMPLETE',
    0x00000001L : 'GSS_S_CONTINUE_NEEDED',
    0x00000002L : 'GSS_S_DUPLICATE_TOKEN',
    0x00000004L : 'GSS_S_OLD_TOKEN',
    0x00000008L : 'GSS_S_UNSEQ_TOKEN',
    0x00000010L : 'GSS_S_GAP_TOKEN',
    0x00010000L : 'GSS_S_BAD_MECH',
    0x00020000L : 'GSS_S_BAD_NAME',
    0x00030000L : 'GSS_S_BAD_NAMETYPE',
    0x00040000L : 'GSS_S_BAD_BINDINGS',
    0x00050000L : 'GSS_S_BAD_STATUS',
    0x00060000L : 'GSS_S_BAD_MIC',
    0x00060000L : 'GSS_S_BAD_SIG',
    0x00070000L : 'GSS_S_NO_CRED',
    0x00080000L : 'GSS_S_NO_CONTEXT',
    0x00090000L : 'GSS_S_DEFECTIVE_TOKEN',
    0x000a0000L : 'GSS_S_DEFECTIVE_CREDENTIAL',
    0x000b0000L : 'GSS_S_CREDENTIALS_EXPIRED',
    0x000c0000L : 'GSS_S_CONTEXT_EXPIRED',
    0x000d0000L : 'GSS_S_FAILURE',
    0x000e0000L : 'GSS_S_BAD_QOP',
    0x000f0000L : 'GSS_S_UNAUTHORIZED',
    0x00100000L : 'GSS_S_UNAVAILABLE',
    0x00110000L : 'GSS_S_DUPLICATE_ELEMENT',
    0x00120000L : 'GSS_S_NAME_NOT_MN',
    0x01000000L : 'GSS_S_CALL_INACCESSIBLE_READ',
    0x02000000L : 'GSS_S_CALL_INACCESSIBLE_WRITE',
    0x03000000L : 'GSS_S_CALL_BAD_STRUCTURE',
}
