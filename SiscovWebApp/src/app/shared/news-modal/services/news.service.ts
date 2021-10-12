import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class NewsService {

  private readonly API = 'http://localhost:5000/'

  constructor(private http: HttpClient) { }

  listAllCountyNews(stateId, countyId) {
    return this.http.get<any>(this.API + 'state/' + stateId + '/county/' + countyId + '/news');
  }

  listAllStateNews(stateId) {
    return this.http.get<any>(this.API + 'state/' + stateId + '/news');
  }

  listAllRegionNews(regionId) {
    return this.http.get<any>(this.API + 'region/' + regionId + '/news');
  }
}
