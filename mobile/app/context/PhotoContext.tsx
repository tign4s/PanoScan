import React, { createContext, useContext,useCallback, ReactNode, useEffect, useState } from 'react';

import { backend_url } from '@/constants/backend_url';
import { useAuth } from './AuthContext';
import api from './ApiContext';

export type Photo = {
  id: number;
  LocalUri: string;
  active: boolean;
  photo: string;
  result: object;
  uploaded_at: string;
  user: number;
};

type PhotoContextType = {
  photos: Photo[];
  fetchPhotos: () => void;
  error: string | null;
};


const PhotoContext = createContext<PhotoContextType | undefined>(undefined);

export const PhotoProvider = ({ children }: { children: ReactNode }) => {
  const [photos, setPhotos] = useState<Photo[]>([]);
  const [error, setError] = useState<string | null>(null);
  const { userId, accessToken, refreshToken, setLoading, setAccessToken, refreshAccessToken} = useAuth();

  const fetchPhotos = useCallback(async () => {
    setError(null)
    try {
      const response = await api.get<Photo[]>(`${backend_url()}user/${userId}/photos/`, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });
      setPhotos(response.data);
    } catch (er:any) {
      if (er.response && er.response.status === 401) {
        try {
          if (refreshToken) {
            const newAccessToken = await refreshAccessToken(refreshToken);
          if (newAccessToken) {
            setAccessToken(newAccessToken)
            const retryResponse = await api.get<Photo[]>(`${backend_url()}user/${userId}/photos/`, {
              headers: {
                Authorization: `Bearer ${newAccessToken}`,
              },
            });
            setPhotos(retryResponse.data);
          } else {
            setError('Failed to refresh access token');
          }
          } else {
            setError('Refresh token missing')
          }
          
        } catch (refreshError) {
          setError('Failed to refresh access token');
        }
      } else {
        console.error('Failed to fetch photos', er);
        setError('Failed to fetch photos');
      }

    } finally {
    }
  }, [userId, refreshAccessToken, setAccessToken]);
  
  
  const handleFetchPhotos = useCallback(async () => {
    if (!userId || !accessToken) {
      console.error('User not authenticated');
      setError('User not authenticated');
      return;
    }
      await fetchPhotos();
  }, [fetchPhotos, userId, accessToken]);

  useEffect(() => {
    if (userId && accessToken) {
      handleFetchPhotos();
    }
  }, [userId, handleFetchPhotos]);

  return (
    <PhotoContext.Provider value={{ photos, fetchPhotos: handleFetchPhotos, error}}>
      {children}
    </PhotoContext.Provider>
  );
};

export const usePhotos = () => {
  const context = useContext(PhotoContext);
  if (!context) {
    throw new Error('usePhotos must be used within a PhotoProvider');
  }
  return context;
};
