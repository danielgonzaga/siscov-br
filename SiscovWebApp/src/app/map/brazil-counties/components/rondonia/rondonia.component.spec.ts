import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RondoniaComponent } from './rondonia.component';

describe('RondoniaComponent', () => {
  let component: RondoniaComponent;
  let fixture: ComponentFixture<RondoniaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RondoniaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RondoniaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
