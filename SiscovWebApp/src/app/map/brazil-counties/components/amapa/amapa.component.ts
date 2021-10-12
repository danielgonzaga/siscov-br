import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-amapa',
  templateUrl: './amapa.component.html',
  styleUrls: ['./amapa.component.css']
})
export class AmapaComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }
}
