import numpy as np
def solveq(K, f, bc):
  """
  Cái này dùng để tìm x, f theo để bài đã cho sẵn 
  Mục đích: Giải hệ phương trình
  Input: Matrix[K], Vector[F]
  Output: x, y, hình vẽ
  Cre: Chân Kiệt (HCMUTE - PoseTona)
  """
  n = K.shape[0]
  dof = np.arange(n)
  ddof = bc[0].astype(int)
  fdof = np.setdiff1d(dof, ddof)
  
  dd = np.ix_(ddof, ddof)
  df = np.ix_(ddof, fdof)
  fd = np.ix_(fdof, ddof)
  ff = np.ix_(fdof, fdof)
  
  d = np.zeros(n)
  d[ddof] = bc[1]
  
  d[fdof] = np.linalg.solve(K[ff], f[fdof] - K[fd] @ d[ddof])
  
  r = np.zeros(n)
  r[ddof] = K[dd] @ d[ddof] + K[df] @ d[fdof]
  return d, r
